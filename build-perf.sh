#!/bin/bash
set -x
#Defaults
#TODO default
MPERFPATH=/home/ace/mongo-perf/
BUILD_DIR=$(pwd)
NUM_CPUS=$(grep ^processor /proc/cpuinfo | wc -l)
RHOST="localhost"
RPORT=28001
BREAK_PATH=/home/ace/stop-build-perf

function do_git_tasks() {
    cd $BUILD_DIR
    git checkout $BRANCH
    git clean -fqdx
    git pull
}

function run_build() {
    cd $BUILD_DIR
    scons -j $NUM_CPUS --mute --opt=off mongod
}


function run_mongo-perf() {
    cd $MPERFPATH
    python runner.py --mongod $BUILD_DIR/mongod --local -l "`date`" --rhost $RHOST --rport $RPORT
}


while true
do
    if [ -e $BREAK_PATH ]
    then
        break
    fi
    do_git_tasks
    run_build
    run_mongo-perf
done
