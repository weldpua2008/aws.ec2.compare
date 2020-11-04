
# Testing module instance_type.g
import pytest
import ec2_compare.internal.instance_type.g

def test_get_internal_data_instance_type_g_get_instances_list():
  assert len(ec2_compare.internal.instance_type.g.get_instances_list()) > 0
def test_get_internal_data_instance_type_g_get():
  assert len(ec2_compare.internal.instance_type.g.get) > 0
