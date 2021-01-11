import pytest
import ec2_compare.mixin
import ec2_compare.internal.ec2data
import ec2_compare.data

def test_ec3__get_rawdata_non_exist():
    inst = ec2_compare.mixin.AwsInstanceMixin()
    assert len(ec2_compare.internal.ec2data.get_instances_list()) == len(inst.ec3__get_rawdata('Non-exists'))

def test_ec3__get_rawdata_exists():
    inst = ec2_compare.mixin.AwsInstanceMixin()
    for k in ['m', 'c', 'r']:
        assert len(ec2_compare.data.get(key='InstanceType', value=k)) == len(inst.ec3__get_rawdata(k))
        assert len(ec2_compare.data.get(key='InstanceType', value=f'{k}5')) < len(inst.ec3__get_rawdata(f'{k}5'))

def test_ec3__get_instances():
    inst = ec2_compare.mixin.AwsInstanceMixin()
    for _fixture in zip(
            [
                {
                    'cpu': 40, 'ram': 786432, 'min_cpu': 8, 'min_ram': 65536,
                    'InstanceType': ['c4', 'c5.', 'r4', 'r5.', 'm4', 'm5.'],
                    'SupportedArchitectures': ['x86_64'], 'SupportedUsageClasses': 'spot'
                },
                {
                    'cpu': 40, 'ram': 786432, 'min_cpu': 8, 'min_ram': 65536,
                    'InstanceType': ['c5.'],
                    'SupportedArchitectures': ['x86_64'], 'SupportedUsageClasses': 'spot'
                },
                {
                    'cpu': 40, 'ram': 786432, 'min_cpu': 8, 'min_ram': 65536,
                    'InstanceType': ['c5.9xlarge'],
                    'SupportedArchitectures': ['x86_64'], 'SupportedUsageClasses': 'spot'
                },
                {
                    'InstanceType': ['c5.9xlarge'],
                }
            ],
            [
                [
                   'c5.9xlarge',
                   'm4.4xlarge',
                   'm5.4xlarge',
                   'm5.8xlarge',
                   'r4.4xlarge',
                   'r4.8xlarge',
                   'r5.2xlarge',
                   'r5.4xlarge',
                   'r5.8xlarge',
                ],
                [
                   'c5.9xlarge',
                ],
                [
                   'c5.9xlarge',
                ],
                [
                   'c5.9xlarge',
                ]
            ]):
        assert inst.ec3__get_instances(**_fixture[0]) == _fixture[1]


def test_ec3__get_machines():
    inst = ec2_compare.mixin.EmrRequestMixin()
    for _fixture in zip(
            [
                {
                    'cpu': 40, 'ram': 786432, 'min_cpu': 8, 'min_ram': 65536,
                    'InstanceType': ['c4', 'c5.', 'r4', 'r5.', 'm4', 'm5.'],
                    'SupportedArchitectures': ['x86_64'], 'SupportedUsageClasses': 'spot'
                },
                {
                    'cpu': 40, 'ram': 786432, 'min_cpu': 8, 'min_ram': 65536,
                    'InstanceType': ['c5.'],
                    'SupportedArchitectures': ['x86_64'], 'SupportedUsageClasses': 'spot'
                },
                {
                    'cpu': 40, 'ram': 786432, 'min_cpu': 8, 'min_ram': 65536,
                    'InstanceType': ['c5.9xlarge'],
                    'SupportedArchitectures': ['x86_64'], 'SupportedUsageClasses': 'spot'
                },
                {
                    'InstanceType': ['c5.9xlarge'],
                }
            ],
            [
                5,
                1,
                1,
                1
            ]):

        assert len(inst.ec3__get_machines(**_fixture[0])) == _fixture[1]
        assert len(inst.ec3__get_machines_for_fleet_request(**_fixture[0])) == _fixture[1]
