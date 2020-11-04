
# Testing module instance_type.z1d
import pytest
import ec2_compare.internal.instance_type.z1d

def test_get_internal_data_instance_type_z1d_get_instances_list():
  assert len(ec2_compare.internal.instance_type.z1d.get_instances_list()) > 0
def test_get_internal_data_instance_type_z1d_get():
  assert len(ec2_compare.internal.instance_type.z1d.get) > 0
