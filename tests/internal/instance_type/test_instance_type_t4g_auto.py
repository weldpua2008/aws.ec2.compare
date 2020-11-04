
# Testing module instance_type.t4g
import pytest
import ec2_compare.internal.instance_type.t4g

def test_get_internal_data_instance_type_t4g_get_instances_list():
  assert len(ec2_compare.internal.instance_type.t4g.get_instances_list()) > 0
def test_get_internal_data_instance_type_t4g_get():
  assert len(ec2_compare.internal.instance_type.t4g.get) > 0
