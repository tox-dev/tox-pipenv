import pytest
from tox_pipenv.plugin import tox_testenv_create
import subprocess
import os
import sys


def test_pcall(venv, mocker):
    mocker.patch.object(os, "environ", autospec=True)
    mocker.patch("subprocess.Popen")
    result = tox_testenv_create(venv, None)
    assert result == True
    subprocess.Popen.assert_called_once_with(
        [sys.executable, "-m", "pipenv", "--python", "test-python"],
        action=None,
        cwd=venv.path.dirpath(),
        venv=False,
    )
    assert venv.tmpdir.ensure("Pipfile")
