.. tox Pipenv documentation master file, created by
   sphinx-quickstart on Mon Jan  8 14:05:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to tox-pipenv's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

What is tox?
------------

tox is a generic virtualenv_ management and test command line tool you can use for:

* checking your package installs correctly with different Python versions and
  interpreters

* running your tests in each of the environments, configuring your test tool of choice

* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

What is Pipenv?
---------------

**Pipenv** — the officially recommended Python packaging tool from `Python.org <https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies>`_, free (as in freedom).

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. *Windows is a first–class citizen, in our world.*

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your ``Pipfile`` as you install/uninstall packages. It also generates the ever–important ``Pipfile.lock``, which is used to produce deterministic builds.

What is tox-pipenv?
-------------------

tox-pipenv is a tox plugin to replace the default use of virtualenv, and pip with Pipenv's development workflow.

This is a convenient way to retain your use of Pipenv, whilst testing multiple versions of Python.

Installation
------------

.. code-block:: bash

    pip install tox-pipenv

Or, 

.. code-block:: bash

    pipenv install tox-pipenv  

Creating virtual environments
-----------------------------

With this plugin, tox will use `pipenv --python {python binary}` as given to the tox interpreter for each python path.

If you already have virtual environments cached with tox, use the --recreate flag to recreate them with pipenv.

Note: tox will pass the --site-packages flag to pipenv if this is configured in your tox config.

The Pipfile will exist in .tox/{env}/Pipfile as well as Pipfile.lock

Installing requirements
-----------------------

The installation of requirements from your tox config will be passed to pipenv install for installation into the virtual 
environment. This replaces the use of pip within tox.

``requirements.txt`` files will also be parsed by Pipenv and used for each test environment

Executing tests
---------------

Each of the commands in your testenv configuration will be passed to pipenv to execute within the pipenv virtual environment
