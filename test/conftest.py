import pytest
import py
import subprocess


class MockConfig(object):
    def __init__(self, tmpdir):
        self._tmpdir = tmpdir

    """
    Fake tox config with static values
    """
    toxinidir = "~/foo"


class MockEnvironmentConfig(object):
    sitepackages = False
    envdir = None


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


class MockAction(object):
    def setactivity(self, *args, **kwargs):
        pass

    def popen(self, *args, **kwargs):
        return subprocess.Popen(*args, **kwargs)


@pytest.fixture
def venv(tmpdir):
    return MockVenv(tmpdir)


@pytest.fixture
def actioncls():
    return MockAction
