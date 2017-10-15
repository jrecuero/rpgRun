#!/bin/bash

source ./setup.sh

export PYTHONPATH=${RPG_RUN_PATH}:${GRAPH_PLAY_PATH}:${JC2LI_PATH}

GRAPH_PLAY_APP=main.py

python ${GRAPH_PLAY_PATH}/${GRAPH_PLAY_APP}
