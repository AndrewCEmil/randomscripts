#!/bin/bash
#Defaults
#TODO build_dir default
MPERFPATH=/home/ace/mongo-perf/
BUILD_DIR=$(pwd)
DB_PATH=/data
MV_PATH=/local/ml
NUM_CPUS=$(grep ^processor /proc/cpuinfo | wc -l)
ERRORLOG=covbuilderrors.log
failedtests[${#failedtests[@]}]="Failed Test List:"
# run every friendly test. quota is not a friendly test. jsPerf isn't anymore either
TEST_PLAN="js clone repl replSets ssl dur auth aggregation failPoint multiVersion disk sharding tool parallel" 


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
