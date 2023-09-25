#!/bin/bash

base_path="week2"

rm test_report.txt

for dir_path in "$base_path"/*; do
    for (( i = 0; i < 5; i++ )); do
      rm "${dir_path}/test_case_new.py"
    done
done


for dir_path in "$base_path"/*; do
    for (( i = 0; i < 5; i++ )); do
      bash ./RunTest.sh "${dir_path}"
    done
done

python3 log_parse.py