#!/bin/bash

source ./setup.sh

py.test . --doctest-modules --ignore=textplay --cov-report html --cov=.
