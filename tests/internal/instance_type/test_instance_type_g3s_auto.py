
# Testing module instance_type.g3s
import pytest
import ec2_compare.internal.instance_type.g3s

def test_get_internal_data_instance_type_g3s_get_instances_list():
  assert len(ec2_compare.internal.instance_type.g3s.get_instances_list()) > 0
def test_get_internal_data_instance_type_g3s_get():
  assert len(ec2_compare.internal.instance_type.g3s.get) > 0
