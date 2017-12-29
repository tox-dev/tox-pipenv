import sys
import os
import tox
from tox import hookimpl
from pipenv.project import Project


@hookimpl
def tox_testenv_create(venv, action):
    pipenv_project = Project()
    pipfile_path = os.path.join(venv.path, 'Pipfile')

    config_interpreter = venv.getsupportedinterpreter()
    args = [sys.executable, '-m', 'pipenv']
    if venv.envconfig.sitepackages:
        args.append('--site-packages')

    args.extend(['--python', str(config_interpreter)])

    venv.session.make_emptydir(venv.path)
    basepath = venv.path.dirpath()
    basepath.ensure(dir=1)
    # Ignore host virtual env
    os.environ['PIPENV_IGNORE_VIRTUALENVS'] = '1'
    # Answer yes on recreation of virtual env
    os.environ['PIPENV_YES'] = '1'
    os.environ['PIPENV_PIPFILE'] = pipfile_path

    with open(pipfile_path, 'a'):
        os.utime(pipfile_path, None)

    # args.append(venv.path.basename)
    venv._pcall(args, venv=False, action=action, cwd=basepath)
    # Return non-None to indicate the plugin has completed
    return True


@hookimpl
def tox_testenv_install_deps(venv, action):
    deps = venv._getresolvedeps()
    if deps:
        os.environ['PIPENV_IGNORE_VIRTUALENVS'] = '1'
        os.environ['PIPENV_PIPFILE'] = os.path.join(venv.path, 'Pipfile')
        # action.setactivity("installdeps", "%s" % depinfo)
        args = [sys.executable, '-m', 'pipenv', 'install', '--dev'] + list(map(str, deps))

        basepath = venv.path.dirpath()
        basepath.ensure(dir=1)
        venv._pcall(args, venv=False, action=action, cwd=basepath)
    # Return non-None to indicate the plugin has completed
    return True


@hookimpl
def tox_runtest(venv, redirect):
    action = venv.session.newaction(venv, "runtests")
    os.environ['PIPENV_IGNORE_VIRTUALENVS'] = '1'
    os.environ['PIPENV_PIPFILE'] = os.path.join(venv.path, 'Pipfile')

    action.setactivity("runtests", "PYTHONHASHSEED=%r" % os.environ.get('PYTHONHASHSEED'))
    for i, argv in enumerate(venv.envconfig.commands):
        # have to make strings as _pcall changes argv[0] to a local()
        # happens if the same environment is invoked twice
        cwd = venv.envconfig.changedir
        message = "commands[%s] | %s" % (i, ' '.join(
            [str(x) for x in argv]))
        action.setactivity("runtests", message)
        # check to see if we need to ignore the return code
        # if so, we need to alter the command line arguments
        if argv[0].startswith("-"):
            ignore_ret = True
            if argv[0] == "-":
                del argv[0]
            else:
                argv[0] = argv[0].lstrip("-")
        else:
            ignore_ret = False
        args = [sys.executable, '-m', 'pipenv', 'run'] + argv
        try:
            venv._pcall(args, venv=False, cwd=cwd, action=action, redirect=redirect,
                        ignore_ret=ignore_ret, testcommand=False)
        except tox.exception.InvocationError as err:
            if venv.envconfig.ignore_outcome:
                venv.session.report.warning(
                    "command failed but result from testenv is ignored\n"
                    "  cmd: %s" % (str(err),))
                venv.status = "ignored failed command"
                continue  # keep processing commands

            venv.session.report.error(str(err))
            venv.status = "commands failed"
            if not venv.envconfig.ignore_errors:
                break  # Don't process remaining commands
        except KeyboardInterrupt:
            venv.status = "keyboardinterrupt"
            venv.session.report.error(venv.status)
            raise
    return True
