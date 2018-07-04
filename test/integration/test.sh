#!/bin/sh

rm -rf env/
virtualenv env --python=python3.7

pip install -e ../../

tox -e py37 -vv
rm -rf env/
