
# Testing module instance_type.m6
import pytest
import ec2_compare.internal.instance_type.m6

def test_get_internal_data_instance_type_m6_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m6.get_instances_list()) > 0
def test_get_internal_data_instance_type_m6_get():
  assert len(ec2_compare.internal.instance_type.m6.get) > 0
