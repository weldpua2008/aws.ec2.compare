
# Testing module instance_type.g5g
import pytest
import ec2_compare.internal.instance_type.g5g

def test_get_internal_data_instance_type_g5g_get_instances_list():
  assert len(ec2_compare.internal.instance_type.g5g.get_instances_list()) > 0
def test_get_internal_data_instance_type_g5g_get():
  assert len(ec2_compare.internal.instance_type.g5g.get) > 0
