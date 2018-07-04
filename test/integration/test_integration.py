import pytest
from tox_pipenv.plugin import tox_testenv_install_deps
import subprocess
import os
import sys
import tox.venv
from tox.config import parseconfig
from tox.session import Session

test_configs = (
    """
[tox]
skipsdist = True
envlist = py36-django{20,master}

[testenv]
commands = pytest --showlocals {posargs}
deps =
	django20: Django>=2.0,<2.1
	djangomaster: https://github.com/django/django/archive/master.tar.gz
	pytest
	pytest-django
    """,
)


@pytest.mark.xfail(reason="not_implemented")
@pytest.mark.parametrize("toxconfig", test_configs)
def test_install_special_deps(toxconfig, mocker, actioncls, tmpdir):
    """
    Test that nothing is called when there are no deps
    """
    action = actioncls()
    p = tmpdir.join("tox.ini")
    p.write(toxconfig)
    with tmpdir.as_cwd():
        config = parseconfig([])

        for env, envconfig in config.envconfigs.items():
            session = Session(config)
            venv = tox.venv.VirtualEnv(envconfig, session=session)
            mocker.patch("subprocess.Popen")
            result = tox_testenv_install_deps(venv, action)
            assert result == True
            assert subprocess.Popen.call_count == 1
            call_list = [sys.executable, "-m", "pipenv", "install", "--dev"]
            call_list.extend([package for package in venv._getresolvedeps()])
            assert subprocess.Popen.call_args_list[0][0] == (call_list,)
