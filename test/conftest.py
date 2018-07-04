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

    @property
    def path(self):
        """ Path to environment base dir. """
        return self.envconfig.envdir

    def getsupportedinterpreter(self):
        return "test-python"

    def _pcall(self, *args, **kwargs):
        return subprocess.Popen(*args, **kwargs)


@pytest.fixture
def venv(tmpdir):
    return MockVenv(tmpdir)
