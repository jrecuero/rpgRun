#!/bin/bash

source ./setup.sh

export PYTHONPATH=${RPG_RUN_PATH}:${JC2LI_PATH}

for file in ./rpgrun/*.py
do
    echo "python -m doctest ${file}"
    python -m doctest $file
done
