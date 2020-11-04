
# Testing module instance_type.z1
import pytest
import ec2_compare.internal.instance_type.z1

def test_get_internal_data_instance_type_z1_get_instances_list():
  assert len(ec2_compare.internal.instance_type.z1.get_instances_list()) > 0
def test_get_internal_data_instance_type_z1_get():
  assert len(ec2_compare.internal.instance_type.z1.get) > 0
