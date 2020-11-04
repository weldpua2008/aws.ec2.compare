
# Testing module instance_type.m4
import pytest
import ec2_compare.internal.instance_type.m4

def test_get_internal_data_instance_type_m4_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m4.get_instances_list()) > 0
def test_get_internal_data_instance_type_m4_get():
  assert len(ec2_compare.internal.instance_type.m4.get) > 0
