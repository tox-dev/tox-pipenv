Release notes
=============

1.9.0 (2019-01-27)
------------------

* Update: Added support for tox 3.7.0 (#60)

1.8.0 (2018-10-30)
------------------

Bugfix : Tox-pipenv would skip the installation of Pipfile if the user had not specified any additional deps in tox.ini (#53)

1.7.0 (2018-10-30)
------------------

* Bugfix : Support for Tox 3.0+
* Bugfix : Fixed API in Tox 3.4.0+
* Bugfix : Removed pinned version which fixes pipenv issue (#50)

1.6.0 (2018-07-04)
------------------

* Bugfix : Tox would fail when executed twice if usedevelop was set to True, reported by @ashwinvis #46
* Bugfix : Any additional dependencies specified in `deps` within tox.ini would be written to the root Pipfile. A temporary Pipfile is created
    for each virtualenv now, which is a clone of the root Pipfile

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
