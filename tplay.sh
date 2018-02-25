#!/bin/bash

source ./setup.sh

export PYTHONPATH=${CURRENT_DIRECTORY}:${RPG_RUN_PATH}:${TEXT_PLAY_PATH}:${JC2CLI_PATH}:${JC2LI_PATH}

TEXT_PLAY_APP=play.py

#python ${TEXT_PLAY_PATH}/${TEXT_PLAY_APP}
#${JC2LI_PATH}/run.sh play.text.play
python ${TEXT_PLAY_PATH}/${TEXT_PLAY_APP}
