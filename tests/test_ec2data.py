import pytest
from ec2_compare import ec2data

def test_get_ec2data():

    assert len(ec2data.get_instances_dict()) > 0
