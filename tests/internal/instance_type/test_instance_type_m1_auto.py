
# Testing module instance_type.m1
import pytest
import ec2_compare.internal.instance_type.m1

def test_get_internal_data_instance_type_m1_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m1.get_instances_list()) > 0
def test_get_internal_data_instance_type_m1_get():
  assert len(ec2_compare.internal.instance_type.m1.get) > 0
