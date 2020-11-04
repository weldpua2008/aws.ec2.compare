
# Testing module instance_type.m5a
import pytest
import ec2_compare.internal.instance_type.m5a

def test_get_internal_data_instance_type_m5a_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m5a.get_instances_list()) > 0
def test_get_internal_data_instance_type_m5a_get():
  assert len(ec2_compare.internal.instance_type.m5a.get) > 0
