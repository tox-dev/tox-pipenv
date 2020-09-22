tox-pipenv
==========

.. image:: https://img.shields.io/pypi/v/tox-pipenv.svg
        :target: https://pypi.python.org/pypi/tox-pipenv

.. image:: https://img.shields.io/travis/tox-dev/tox-pipenv.svg
        :target: https://travis-ci.org/tox-dev/tox-pipenv

.. image:: https://codecov.io/gh/tox-dev/tox-pipenv/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/tox-dev/tox-pipenv

.. image:: https://pyup.io/repos/github/tox-dev/tox-pipenv/shield.svg
     :target: https://pyup.io/repos/github/tox-dev/tox-pipenv/
     :alt: Updates

.. image:: https://pyup.io/repos/github/tox-dev/tox-pipenv/python-3-shield.svg
     :target: https://pyup.io/repos/github/tox-dev/tox-pipenv/
     :alt: Python 3

A tox plugin to replace the default use of virtualenv with Pipenv.

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

Example tox.ini
---------------

This simple example will test against Python 2.7 and 3.6 using pytest to execute the tests.

.. code-block:: 

        [tox]
        envlist = py27, py36

        [testenv]
        deps = 
            pytest
            pytest-mock
        commands = python -m pytest test/


Frequently asked questions
--------------------------

Where to install
~~~~~~~~~~~~~~~~

Tox-Pipenv should be installed in the same environment as Tox, whether that is in a virtualenvironment, system environment or user environment. Tox-Pipenv depends on
Tox 3.0 or newer.

Is user expected to create `Pipfile` and `Pipfile.lock` before executing `tox` with this plugin?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, although if you are migrating from a requirements.txt to a Pipfile, you can use Pipenv to create the Pipfile for you.

Is `Pipfile.lock` expected to be under source control?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

According to `pipenv` documentation, `Pipfile.lock` is not recommended under source control if it is going to be used under multiple Python versions.

What is the role of `requirements.txt` file?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often, `tox` users use `requirements.txt` which is then referenced from within `tox.ini` file as deps. Pipenv will automatically install any packages listed in 
`requirements.txt` for each virtual environment that Tox creates.

Is `tox.ini` `deps` section really in control?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, this is a known limitation. 


Authors
-------

* Anthony Shaw
* Omer Katz
* Almog Cohen
