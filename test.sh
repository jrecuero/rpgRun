#!/bin/bash

source ./setup.sh

py.test test/ --doctest-modules --ignore=textplay --cov-report html --cov=./rpgrun
