
# Testing module instance_type.m5zn
import pytest
import ec2_compare.internal.instance_type.m5zn

def test_get_internal_data_instance_type_m5zn_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m5zn.get_instances_list()) > 0
def test_get_internal_data_instance_type_m5zn_get():
  assert len(ec2_compare.internal.instance_type.m5zn.get) > 0
