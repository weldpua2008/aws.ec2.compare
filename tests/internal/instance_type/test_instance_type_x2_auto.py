
# Testing module instance_type.x2
import pytest
import ec2_compare.internal.instance_type.x2

def test_get_internal_data_instance_type_x2_get_instances_list():
  assert len(ec2_compare.internal.instance_type.x2.get_instances_list()) > 0
def test_get_internal_data_instance_type_x2_get():
  assert len(ec2_compare.internal.instance_type.x2.get) > 0
