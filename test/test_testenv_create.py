import pytest
from tox_pipenv.plugin import tox_testenv_create
import subprocess
import os
import sys


def test_pcall(venv, mocker, actioncls):
    action = actioncls()
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    result = tox_testenv_create(venv, action)
    assert result == True

    # Check that pipenv was executed with the correct arguments
    subprocess.Popen.assert_called_once_with(
        [sys.executable, "-m", "pipenv", "--python", "test-python"],
        action=action,
        cwd=venv.path.dirpath(),
        venv=False,
    )
    assert venv.tmpdir.ensure("Pipfile")


def test_pcall_sitepackages(venv, mocker, actioncls):
    """
    Check that the sitepackages configuration in tox is passed to pipenv
    """
    action = actioncls()
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    venv.envconfig.sitepackages = True
    result = tox_testenv_create(venv, action)
    assert result == True

    # Check that pipenv was executed with the correct arguments
    subprocess.Popen.assert_called_once_with(
        [sys.executable, "-m", "pipenv", "--site-packages", "--python", "test-python"],
        action=action,
        cwd=venv.path.dirpath(),
        venv=False,
    )
    assert venv.tmpdir.ensure("Pipfile")
