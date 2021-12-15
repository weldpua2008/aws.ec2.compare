
# Testing module instance_type.mac1
import pytest
import ec2_compare.internal.instance_type.mac1

def test_get_internal_data_instance_type_mac1_get_instances_list():
  assert len(ec2_compare.internal.instance_type.mac1.get_instances_list()) > 0
def test_get_internal_data_instance_type_mac1_get():
  assert len(ec2_compare.internal.instance_type.mac1.get) > 0
