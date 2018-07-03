#!/bin/sh

rm -rf env/
virtualenv env --python=python3.7

pip install -e ../../

pipenv run tox -e py37