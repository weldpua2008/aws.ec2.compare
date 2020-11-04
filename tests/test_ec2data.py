import pytest
import ec2_compare.internal.ec2data

def test_get_ec2data():
    assert len(ec2_compare.internal.ec2data.get_instances_list()) > 0
