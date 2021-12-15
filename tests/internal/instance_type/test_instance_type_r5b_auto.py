
# Testing module instance_type.r5b
import pytest
import ec2_compare.internal.instance_type.r5b

def test_get_internal_data_instance_type_r5b_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r5b.get_instances_list()) > 0
def test_get_internal_data_instance_type_r5b_get():
  assert len(ec2_compare.internal.instance_type.r5b.get) > 0
