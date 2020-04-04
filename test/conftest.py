import pytest
import py
import subprocess
import os

from _pytest.tmpdir import tmpdir


class MockConfig(object):
    def __init__(self, tmpdir):
        self._tmpdir = tmpdir

    """
    Fake tox config with static values
    """
    toxinidir = os.curdir


class MockEnvironmentConfig(object):
    sitepackages = False
    envdir = None
    pip_pre = False


class MockSession(object):
    def __init__(self, tmpdir):
        self.config = MockConfig(tmpdir)
        self.config.toxinidir = tmpdir

    def make_emptydir(self, path):
        return True


class MockVenv(object):
    def __init__(self, tmpdir, *args, **kwargs):
        self.tmpdir = tmpdir
        self.session = MockSession(tmpdir)
        self.envconfig = MockEnvironmentConfig()
        self.envconfig.envdir = tmpdir
        self.deps = []

    @property
    def path(self):
        """ Path to environment base dir. """
        return self.envconfig.envdir

    def getsupportedinterpreter(self):
        return "test-python"

    def _pcall(self, *args, **kwargs):
        return subprocess.Popen(*args, **kwargs)

    def _getresolvedeps(self):
        return self.deps

    def get_resolved_dependencies(self):
        # _getresolvedeps was deprecated on tox 3.7.0 in favor of get_resolved_dependencies
        return self.deps


class MockAction(object):
    def __init__(self, venv=None):
        self.venv = venv

    def setactivity(self, *args, **kwargs):
        pass

    def popen(self, *args, **kwargs):
        return subprocess.Popen(*args, **kwargs)


@pytest.fixture
def venv(tmpdir):
    venv = MockVenv(tmpdir)
    return  venv


@pytest.fixture
def actioncls():
    return MockAction
