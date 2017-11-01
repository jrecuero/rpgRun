#!/bin/bash

CURRENT_DIR=`pwd`
REPO_PATH=${HOME}/Repository
APP_PATH=${REPO_PATH}/rpgRun
JC2LI_PATH=${REPO_PATH}/jc2li
PYGAME_PATH=/Users/jorecuer/virtualenv/python3/lib/python3.6/site-packages

export PYTHONPATH=$PYTHONPATH:$APP_PATH:$JC2LI_PATH:$PYGAME_PATH

vim $1
