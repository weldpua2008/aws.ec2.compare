#!/usr/bin/env bash
export PYTHON_VERSION=${PYTHON_VERSION:-}
export VERSION=${VERSION:-}

echo "#########################################################################"
echo "###############  BUILD with Python ${PYTHON_VERSION:-} ##################"
echo "#########################################################################"
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
    && python${PYTHON_VERSION} setup.py build sdist bdist_wheel \
    && export _VERSION=$(cat version.txt || echo $VERSION) \
    && export VERSION=${__VERSION:-$VERSION} \
    && export PACKAGE_VERSION=${VERSION} \
    && twine upload --disable-progress-bar --non-interactive --skip-existing  dist/*\
    && cd -

    exit_code=$?

# for py in "2.7" "3.6" "3.7" "3.8" "3.9";do
#  docker run -ti --rm python:${py} bash -c "
#  pip install ec2-compare && python -c 'import sys;from ec2_compare import ec2data; sys.exit(127) if not ec2data.get_instances_dict() else print(\"${py} is OK\")'
#  "
# done
exit ${exit_code:-127}
