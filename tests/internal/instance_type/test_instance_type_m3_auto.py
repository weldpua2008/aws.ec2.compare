
# Testing module instance_type.m3
import pytest
import ec2_compare.internal.instance_type.m3

def test_get_internal_data_instance_type_m3_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m3.get_instances_list()) > 0
def test_get_internal_data_instance_type_m3_get():
  assert len(ec2_compare.internal.instance_type.m3.get) > 0
