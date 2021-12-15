
# Testing module instance_type.is
import pytest
import ec2_compare.internal.instance_type.is

def test_get_internal_data_instance_type_is_get_instances_list():
  assert len(ec2_compare.internal.instance_type.is.get_instances_list()) > 0
def test_get_internal_data_instance_type_is_get():
  assert len(ec2_compare.internal.instance_type.is.get) > 0
