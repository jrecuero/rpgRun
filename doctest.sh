#!/bin/bash

source ./setup.sh

export PYTHONPATH=${RPG_RUN_PATH}:${JC2LI_PATH}

if [ $# -eq 0 ]
then
    for file in ./rpgrun/common/*.py ./rpgrun/board/*.py ./rpgrun/game/*.py
    do
        echo "python -m doctest ${file}"
        python -m doctest $file
    done
else
    echo "python -m doctest $1"
    python -m doctest $1
fi

