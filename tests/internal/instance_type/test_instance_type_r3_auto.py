
# Testing module instance_type.r3
import pytest
import ec2_compare.internal.instance_type.r3

def test_get_internal_data_instance_type_r3_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r3.get_instances_list()) > 0
def test_get_internal_data_instance_type_r3_get():
  assert len(ec2_compare.internal.instance_type.r3.get) > 0
