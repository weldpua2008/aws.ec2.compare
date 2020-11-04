
# Testing module instance_type.d
import pytest
import ec2_compare.internal.instance_type.d

def test_get_internal_data_instance_type_d_get_instances_list():
  assert len(ec2_compare.internal.instance_type.d.get_instances_list()) > 0
def test_get_internal_data_instance_type_d_get():
  assert len(ec2_compare.internal.instance_type.d.get) > 0
