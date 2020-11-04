
# Testing module instance_type.t4
import pytest
import ec2_compare.internal.instance_type.t4

def test_get_internal_data_instance_type_t4_get_instances_list():
  assert len(ec2_compare.internal.instance_type.t4.get_instances_list()) > 0
def test_get_internal_data_instance_type_t4_get():
  assert len(ec2_compare.internal.instance_type.t4.get) > 0
