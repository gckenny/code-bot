#!/bin/bash
dir_path=$1

echo "========= ${dir_path} ==========="
# record start time

start=`date +%s`
is_need_to_run=1
# check is there a test_case.py
if [ -f "${dir_path}/test_case_new.py" ]; then
    echo "test_case_new.py exists, check if it is OK"
    gtimeout 1 python3 "${dir_path}"/test_case_new.py 2> "${dir_path}/test_case_result.log"
    test_case_result=$(cat "${dir_path}/test_case_result.log"| tail -1)
    echo "test_case_result: ${test_case_result}"
    if [ "${test_case_result}" == "OK" ]; then
        echo "\"${dir_path}\"" " result: Success: 0s, 1, ${test_case_result}" >> test_report.txt
        is_need_to_run=0
    fi
fi
if [ "${is_need_to_run}" == "1" ]; then
    echo "is_need_to_run, run main.py"
    gtimeout 60 python3 main.py --debug --question-path "${dir_path}"
    # record end time
    end=`date +%s`

    rm ${dir_path}/test_case_result.log
    # calculate execution time
    runtime=$( echo "$end - $start" | bc -l )
    echo "runtime: $runtime"
    cat "${dir_path}/test_case.py" | sed 's/def solution/def fake_solution/g' > "${dir_path}/test_case_new.py"
    cat "./solutions/solution.py" >> "${dir_path}/test_case_new.py"
    echo -e "\n\nif __name__ == '__main__':\n    unittest.main()" >> "${dir_path}/test_case_new.py"
    gtimeout 1 python3 "${dir_path}"/test_case_new.py 2> "${dir_path}/test_case_result.log"
    test_case_result=$(cat "${dir_path}/test_case_result.log"| tail -1)
    test_cast_count=$(cat "${dir_path}/test_case_result.log"| tail -3 | head -1)
    if [ $? -eq 0 ]; then
        echo "\"${dir_path}\"" " result: Success: ${runtime}s, ${test_cast_count}, ${test_case_result}" >> test_report.txt
    else
        echo "\"${dir_path}\"" " result: Failed: ${runtime}s, ${test_cast_count}, ${test_case_result}" >> test_report.txt
    fi
fi