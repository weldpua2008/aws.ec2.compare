
# Testing module instance_type.c
import pytest
import ec2_compare.internal.instance_type.c

def test_get_internal_data_instance_type_c_get_instances_list():
  assert len(ec2_compare.internal.instance_type.c.get_instances_list()) > 0
def test_get_internal_data_instance_type_c_get():
  assert len(ec2_compare.internal.instance_type.c.get) > 0
