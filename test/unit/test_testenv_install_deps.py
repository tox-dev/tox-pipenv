import pytest
from tox_pipenv.plugin import tox_testenv_install_deps
import subprocess
import os
import sys


def test_install_no_deps(venv, mocker, actioncls):
    """
    Test that nothing is called when there are no deps
    """
    action = actioncls()
    venv.deps = []
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    result = tox_testenv_install_deps(venv, action)
    assert result == True
    assert subprocess.Popen.call_count == 0


def test_install_special_deps(venv, mocker, actioncls):
    """
    Test that nothing is called when there are no deps
    """
    action = actioncls()
    venv.deps = ["foo-package", "foo-two-package"]
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    result = tox_testenv_install_deps(venv, action)
    assert result == True
    assert subprocess.Popen.call_count == 1
    subprocess.Popen.assert_called_once_with(
        [
            sys.executable,
            "-m",
            "pipenv",
            "install",
            "--dev",
            "foo-package",
            "foo-two-package",
        ],
        action=action,
        cwd=venv.path.dirpath(),
        venv=False,
    )
