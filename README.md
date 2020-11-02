# aws.ec2.compare
Compare EC2 instances families without querying AWS API

## Update data
1. Downland the latest info
````bash
aws ec2 describe-instance-types | jq '.InstanceTypes' > aws_ec2.json
````
2. repack
```bash
python3 repack.py
```
