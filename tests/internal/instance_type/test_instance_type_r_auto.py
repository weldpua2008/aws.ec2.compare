
# Testing module instance_type.r
import pytest
import ec2_compare.internal.instance_type.r

def test_get_internal_data_instance_type_r_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r.get_instances_list()) > 0
def test_get_internal_data_instance_type_r_get():
  assert len(ec2_compare.internal.instance_type.r.get) > 0
