lcov -t $1 -o ./raw-test.info -c -d ./build/darwin/gcov/mongo/ -b src/mongo --derive-func-data --rc lcov_branch_coverage=1
lcov --extract ./raw-test.info \*mongo/src/mongo\* -o lcov-test.info --rc lcov_branch_coverage=1
genhtml -s -o ./testout-coverage -t "test" --highlight lcov-test.info --rc lcov_branch_coverage=1
