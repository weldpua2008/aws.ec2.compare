#!/usr/bin/env bash
#
# Update ec2data
#
: "${CLEANUP_CACHE:=yes}"
START_TIME=$(date +%s)

cd $(dirname "$0")

function on_exit(){
    local _exit_code=${1:-1}
    local runtime=$(($(date +%s) - START_TIME))
    echo "++++++++++++++++++++++++++++++++++++++++++++++
Took ${runtime} seconds to execute
++++++++++++++++++++++++++++++++++++++++++++++"
    if [[ "${CLEANUP_CACHE}" = "yes" ]] && [[ -e ./aws_ec2.json ]];then
        echo "Removing cached json"
        rm -f ./aws_ec2.json
    fi
    exit ${_exit_code}

}

trap 'on_exit $?' EXIT HUP TERM INT

echo "Downloading instance types via cli at ${PWD}"
aws ec2 describe-instance-types  | python3 -c "import sys, json, operator; d=json.load(sys.stdin)['InstanceTypes']; d.sort(key=operator.itemgetter('InstanceType')); json.dump(d, sys.stdout, indent=4) if d else sys.exit(127)" > ./aws_ec2.json \
&& echo "Recreate ec2data.py" \
&& python3 redownload.py \
&& echo "Succeess"
