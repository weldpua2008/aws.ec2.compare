#!/usr/bin/env bash
# Update ec2data
cd $(dirname "$0")
# aws ec2 describe-instance-types | jq '.InstanceTypes' > aws_ec2.json
START_TIME=$(date +%s)
function on_exit(){
    local _exit_code=${1:-1}
    local runtime=$(($(date +%s) - START_TIME))
    echo "++++++++++++++++++++++++++++++++++++++++++++++
Took ${runtime} seconds to execute
++++++++++++++++++++++++++++++++++++++++++++++"
    if [[ -e ./aws_ec2.json ]];then
        echo "Removing cached json"
        rm -f ./aws_ec2.json
    fi
    exit ${_exit_code}

}

trap 'on_exit $?' EXIT HUP TERM INT

echo "Downloading instance types via cli"
aws ec2 describe-instance-types  | python3 -c "import sys, json; d=json.load(sys.stdin)['InstanceTypes']; json.dump(d, sys.stdout) if d else sys.exit(127)" > ./aws_ec2.json \
&& echo "Recreate ec2data.py" \
&& python3 redownload.py \
&& echo "Succeess"
