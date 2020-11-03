#!/usr/bin/env bash
echo "##########################################"
echo "###############  BUILD  ##################"
echo "##########################################"
export LC_ALL="en_US.UTF-8" 2> /dev/null

export OUTPUT_PATH="./release_folder"
START_TIME=$(date +%s)
function _post(){
    if [[ -e "${OUTPUT_PATH}" ]];then
        rm -rf "${OUTPUT_PATH}"
    fi
    rm -rf build *.egg-info dist dist/* version.txt
}

function _pre(){
    _post
    mkdir -p "${OUTPUT_PATH}"
}

function on_exit(){
    local _exit_code=${1:-1}
    local runtime=$(($(date +%s) - START_TIME))
    _post
    if [[ ${_exit_code} -eq 0 ]];then
        _msg="\n\Succeess\n"
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

cd $(dirname "$0")/.. \
    && pwd \
    && _pre \
    && python setup.py build sdist bdist_wheel \
    && twine upload --repository-url http://localhost:8080/ --username user --password pass --non-interactive dist/*\
    && cd -

    exit_code=$?
exit ${exit_code:-127}
