#!/bin/bash

CURRENT_DIRECTORY=`pwd`
REPO_PATH=${CURRENT_DIRECTORY}/..
JC2LI_PATH=${REPO_PATH}/jc2li
RPG_RUN_PATH=${REPO_PATH}/rpgRun
TEXT_PLAY_PATH=${RPG_RUN_PATH}/textplay

export PYTHONPATH=${RPG_RUN_PATH}:${TEXT_PLAY_PATH}:${JC2LI_PATH}
