
# Testing module instance_type.r6
import pytest
import ec2_compare.internal.instance_type.r6

def test_get_internal_data_instance_type_r6_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r6.get_instances_list()) > 0
def test_get_internal_data_instance_type_r6_get():
  assert len(ec2_compare.internal.instance_type.r6.get) > 0
