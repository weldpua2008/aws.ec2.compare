
# Testing module instance_type.r5
import pytest
import ec2_compare.internal.instance_type.r5

def test_get_internal_data_instance_type_r5_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r5.get_instances_list()) > 0
def test_get_internal_data_instance_type_r5_get():
  assert len(ec2_compare.internal.instance_type.r5.get) > 0
