
# Testing module instance_type.m6a
import pytest
import ec2_compare.internal.instance_type.m6a

def test_get_internal_data_instance_type_m6a_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m6a.get_instances_list()) > 0
def test_get_internal_data_instance_type_m6a_get():
  assert len(ec2_compare.internal.instance_type.m6a.get) > 0
