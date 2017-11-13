#!/bin/bash

source ./setup.sh

export PYTHONPATH=${CURRENT_DIRECTORY}:${JC2LI_PATH}

# py.test test/ --doctest-modules --ignore=textplay --cov-report html --cov=./rpgrun
py.test ./rpgrun/ --doctest-modules --ignore=textplay --cov-report html --cov=./rpgrun
