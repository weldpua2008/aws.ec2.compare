#!/usr/bin/env bash
echo "##########################################"
echo "###############   TESTS ##################"
echo "##########################################"
export LC_ALL="en_US.UTF-8" 2> /dev/null
export PYTHONPATH=$PYTHONPATH:..:../ec2_compare:../ec2_compare

START_TIME=$(date +%s)
function on_exit(){
    local _exit_code=${1:-1}
    local runtime=$(($(date +%s) - START_TIME))
    if [[ ${_exit_code} -eq 0 ]];then
        _msg="\n\nAll tests passed\n"
    fi
    echo -e "++++++++++++++++++++++++++++++++++++++++++++++
Took ${runtime} seconds to execute ${_msg:-}
Exit code: ${_exit_code}
++++++++++++++++++++++++++++++++++++++++++++++"
    exit ${_exit_code}

}
trap 'on_exit $?' EXIT HUP TERM INT
find . -name '__pycache__' -type d -exec rm -rf {} \; 2> /dev/null || true

set -e

###### Main

cd $(dirname "$0") \
    && cd ../tests \
    && echo "Running pytest" \
    && pytest --cov=./ --cov-report=xml $@ \
    && echo -e "\nCheck if there are Python syntax errors or undefined names\n" >&2 \
    && flake8 ../ec2_compare \
        --max-complexity=10 \
        --max-line-length=127 \
        --select=E9,F63,F7,F82 \
        --show-source \
        --statistics \
    && echo "Running mypy" >&2 \
    && mypy ../ec2_compare \
    && echo "Running pylint" >&2 \
    && pylint ../ec2_compare


    exit_code=$?
exit ${exit_code:-127}
