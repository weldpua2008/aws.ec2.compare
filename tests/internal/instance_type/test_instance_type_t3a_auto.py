
# Testing module instance_type.t3a
import pytest
import ec2_compare.internal.instance_type.t3a

def test_get_internal_data_instance_type_t3a_get_instances_list():
  assert len(ec2_compare.internal.instance_type.t3a.get_instances_list()) > 0
def test_get_internal_data_instance_type_t3a_get():
  assert len(ec2_compare.internal.instance_type.t3a.get) > 0
