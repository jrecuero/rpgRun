#!/bin/bash

CURRENT_DIR=`pwd`
REPO_PATH=${HOME}/Repository
APP_PATH=REPO_PATH/rpgRun
PYGAME_PATH=/Users/jorecuer/virtualenv/python3/lib/python3.6/site-packages

export PYTHONPATH=$PYTHONPATH:$PYGAME_PATH

vim $1
