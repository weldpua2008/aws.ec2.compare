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
set -e

###### Main

cd $(dirname "$0") \
    && cd ../tests \
    && pytest --cov=./ --cov-report=xml $@ \
    && echo -e "\nStop the build if there are Python syntax errors or undefined names\n" >&2 \
    && flake8 ../ec2_compare \
        --max-complexity=10 \
        --max-line-length=127 \
        --select=E9,F63,F7,F82 \
        --show-source \
        --statistics \
    && mypy ../ec2_compare \
    && pylint ../ec2_compare


    exit_code=$?
exit ${exit_code:-127}
