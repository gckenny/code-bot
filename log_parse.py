import json
import re

test_results = {}

with open('test_report.txt', 'r') as file:
    lines = file.readlines()

map = {}

for line in lines:
    try:
        parts = line.strip().split(",")
        case_name = parts[0]
        case_name_part = case_name.split(" ")
        case_id = case_name_part[0][1:]
        if case_name_part[-1][:-1] == "":
            case_time = 0
        else:
            case_time = float(case_name_part[-1][:-1])
        test_case_part = parts[1].split(" ")
        if test_case_part[2] == "":
            total_test_case = 1
        else:
            total_test_case = int(test_case_part[2])
        test_case_status = parts[2]
        success_case = 0
        error_case = 0
        fail_case = 0
        if "OK" == test_case_status:
            success_case = int(total_test_case)
        if "failures" in test_case_status:
            fail_case = int(re.search(r'failures=(\d+)', test_case_status).group(1))
        if "error" in test_case_status:
            error_case = int(re.search(r'errors=(\d+)', test_case_status).group(1))
        success_case = total_test_case - fail_case - error_case
        if case_id in map:
            max_success_case = max(success_case, map[case_id].get("max_success_case", 0))
            map.update({
                case_id: {
                    "case_time": case_time + map[case_id].get("case_time", 0),
                    "total_test_case": total_test_case + map[case_id].get("total_test_case", 0),
                    "fail_case": fail_case + map[case_id].get("fail_case", 0),
                    "error_case": error_case + map[case_id].get("error_case", 0),
                    "success_case": success_case + map[case_id].get("success_case", 0),
                    "total_round": map[case_id].get("total_round", 0) + 1,
                    "max_success_case": max_success_case,
                    "max_score": max_success_case / map[case_id].get("one_round_test_case", 0),
                    "one_round_test_case": max(total_test_case, map[case_id].get("one_round_test_case", 0))
                }
            })
        else:
            max_success_case = max(success_case, 0)
            map.update({
                case_id: {
                    "case_time": case_time,
                    "total_test_case": total_test_case,
                    "fail_case": fail_case,
                    "error_case": error_case,
                    "success_case": success_case,
                    "total_round": 1,
                    "max_success_case": max_success_case,
                    "max_score": max_success_case / total_test_case,
                    "one_round_test_case": total_test_case,
                }
            })
    except Exception as e:
        print(e)

for case_id in map:
    map[case_id].update({
        "average_run_time": map[case_id].get("case_time", 0) / map[case_id].get("total_round", 0),
        "pass_rate": map[case_id].get("success_case", 0) / map[case_id].get("total_test_case", 0),
    })
pretty_map = json.dumps(map, indent=4)
with open("test_report_total.txt", "w") as file:
    file.write(pretty_map)
    total_pass_rate = 0
    total_max_success_case = 0
    total_max_score = 0
    for case_id in map:
        total_pass_rate += map[case_id].get("pass_rate", 0)
        total_max_success_case += map[case_id].get("max_success_case", 0)
        total_max_score += map[case_id].get("max_score", 0)
    file.write(f"\n")
    file.write(f"average pass rate: {total_pass_rate / len(map)}")
    file.write(f"\n")
    file.write(f"pass success case number: {total_max_success_case}")
    file.write(f"\n")
    file.write(f"average all pass case number: {total_max_success_case / len(map)}")
    file.write(f"\n")
    file.write(f"normalize score: {total_max_score}")
    file.write(f"\n")
    file.write(f"average round normalize score: {total_max_score / len(map)}")
