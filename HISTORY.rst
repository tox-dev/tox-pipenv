Release notes
=============

1.2.0 (2018-01-08)
------------------

* Virtual environments are now correctly stored in .tox/<pyver>/.venv
* Packages will be reported by pipenv graph after installation. Pip freeze is still being run, downstream PR raised in tox
* Plugin should not accidentally remove host virtualenv binaries

1.1.0 (2017-12-30)
------------------

* Use Pipenv install --dev as the default installation command

1.0.0 (2017-12-22)
------------------

* Support for creation and recreation of virtual environments using Pipenv
* Isolation of Pipfile within the tox directory
* Support for installation of tox-specified packages in Pipenv
* Support for execution of test commands within a Pipenv virtual env