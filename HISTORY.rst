Release notes
=============

1.5.0 (2018-07-03)
------------------

* Update : Update tox to 3.0.0
* Feature : Tox report now uses pipenv instead of pip freeze
* Bugfix : Fixed issue on newer versions of pipenv raising error "AttributeError: 'Project' object has no attribute 'pipfile_sources'" (#41)

1.4.1 (2018-03-15)
------------------

* Removed test virtualenv from package, meaning distribution was 18MB, should be 15Kb #38

1.4.0 (2018-03-08)
------------------

* Bugfix : Fixed error "LocalPath object has no attribute endswith"
* Bugfix : Fixed error "Cannot run tox for the first time with this plugin installed"

1.3.0 (2018-03-03)
------------------

* Bugfix : fixed issue when Pathlib.Path occured instead of string
* Update : updated pipenv to 11.0.1

1.2.1 (2018-01-08)
------------------

* Added documentation and fixed pypi build

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
