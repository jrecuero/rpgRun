#!/bin/bash

source ./setup.sh

for file in ./*.py
do
    echo "python -m doctest ${file}"
    python -m doctest $file
done
