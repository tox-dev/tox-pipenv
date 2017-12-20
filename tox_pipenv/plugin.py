import sys
from tox import hookimpl
import pipenv


@hookimpl
def tox_testenv_create(venv, action):
    config_interpreter = venv.getsupportedinterpreter()
    args = [sys.executable, '-m', 'pipenv']
    if venv.envconfig.sitepackages:
        args.append('--site-packages')

    args.extend(['--python', str(config_interpreter)])

    venv.session.make_emptydir(venv.path)
    basepath = venv.path.dirpath()
    basepath.ensure(dir=1)
    # args.append(venv.path.basename)
    venv._pcall(args, venv=False, action=action, cwd=basepath)
    # Return non-None to indicate the plugin has completed
    return True


@hookimpl
def tox_get_python_executable(envconfig):
    pass


@hookimpl
def tox_testenv_install_deps(venv, action):
    deps = venv._getresolvedeps()
    if deps:
        depinfo = " ".join(map(str, deps))
        action.setactivity("installdeps", "%s" % depinfo)
        config_interpreter = venv.getsupportedinterpreter()
        args = [sys.executable, '-m', 'pipenv', 'install']

        basepath = venv.path.dirpath()
        basepath.ensure(dir=1)
        venv._pcall(args, venv=False, action=action, cwd=basepath)
    # Return non-None to indicate the plugin has completed
    return True


@hookimpl
def tox_runtest(venv, redirect):
    venv.test(redirect=redirect)
    # Return non-None to indicate the plugin has completed
    return True