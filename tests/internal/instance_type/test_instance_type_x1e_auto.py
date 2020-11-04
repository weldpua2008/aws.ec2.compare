
# Testing module instance_type.x1e
import pytest
import ec2_compare.internal.instance_type.x1e

def test_get_internal_data_instance_type_x1e_get_instances_list():
  assert len(ec2_compare.internal.instance_type.x1e.get_instances_list()) > 0
def test_get_internal_data_instance_type_x1e_get():
  assert len(ec2_compare.internal.instance_type.x1e.get) > 0
