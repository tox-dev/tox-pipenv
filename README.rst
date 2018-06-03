tox-pipenv
==========

.. image:: https://img.shields.io/pypi/v/tox-pipenv.svg
        :target: https://pypi.python.org/pypi/tox-pipenv

.. image:: https://img.shields.io/travis/tonybaloney/tox-pipenv.svg
        :target: https://travis-ci.org/tonybaloney/tox-pipenv

.. image:: https://codecov.io/gh/tonybaloney/tox-pipenv/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/tonybaloney/tox-pipenv

.. image:: https://pyup.io/repos/github/tonybaloney/tox-pipenv/shield.svg
     :target: https://pyup.io/repos/github/tonybaloney/tox-pipenv/
     :alt: Updates

.. image:: https://pyup.io/repos/github/tonybaloney/tox-pipenv/python-3-shield.svg
     :target: https://pyup.io/repos/github/tonybaloney/tox-pipenv/
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


TODO
----

This plugin needs work, namely: 

* tox always calls `pip freeze` to show versions, this is not yet pluggable

Authors
-------

* Anthony Shaw
* Omer Katz