#!/bin/bash

CURRENT_DIR=`pwd`
REPO_PATH=${HOME}/Repository
RPGRUN_PATH=${REPO_PATH}/rpgRun
GRAPH_APP_PATH=${RPGRUN_PATH}/play/graph
JC2LI_PATH=${REPO_PATH}/jc2li
PYGAME_PATH=/Users/jorecuer/virtualenv/python3/lib/python3.6/site-packages

export PYTHONPATH=$PYTHONPATH:$RPGRUN_PATH:$GRAPH_APP_PATH:$JC2LI_PATH:$PYGAME_PATH

vim $1
