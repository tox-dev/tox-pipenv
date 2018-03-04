#!/bin/sh

rm -rf env/
virtualenv env --python=python3.6

pip install -e ../../

pipenv run tox