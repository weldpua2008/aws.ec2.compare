
# Testing module instance_type.r5a
import pytest
import ec2_compare.internal.instance_type.r5a

def test_get_internal_data_instance_type_r5a_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r5a.get_instances_list()) > 0
def test_get_internal_data_instance_type_r5a_get():
  assert len(ec2_compare.internal.instance_type.r5a.get) > 0
