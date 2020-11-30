#!/usr/bin/env bash
cd $(dirname "$0")
docker build -t local/aws.ec2.compare.github .
