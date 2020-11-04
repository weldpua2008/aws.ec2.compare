
# Testing module instance_type.c6g
import pytest
import ec2_compare.internal.instance_type.c6g

def test_get_internal_data_instance_type_c6g_get_instances_list():
  assert len(ec2_compare.internal.instance_type.c6g.get_instances_list()) > 0
def test_get_internal_data_instance_type_c6g_get():
  assert len(ec2_compare.internal.instance_type.c6g.get) > 0
