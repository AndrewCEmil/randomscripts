#!/bin/bash
#Defaults
#TODO default
MPERFPATH=/home/ace/mongo-perf/
BUILD_DIR=$(pwd)
NUM_CPUS=$(grep ^processor /proc/cpuinfo | wc -l)

function do_git_tasks() {
    cd $BUILD_DIR
    git checkout $BRANCH
    git clean -fqdx
    git pull
}

function run_build() {
    cd $BUILD_DIR
    scons -j $NUM_CPUS --mute --opt=off 
}


function run_mongo-perf() {
    cd $MPERFPATH
    python runner.py --mongod $BUILD_DIR/mongod --local -l `date` --rhost localhost --rport 28001
}


while true
do
    if [ -e $BREAK_PATH ]
    then
        break
    fi
    do_git_tasks
    run_build
    run_mongo_perf
done
