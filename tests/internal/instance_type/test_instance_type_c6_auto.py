
# Testing module instance_type.c6
import pytest
import ec2_compare.internal.instance_type.c6

def test_get_internal_data_instance_type_c6_get_instances_list():
  assert len(ec2_compare.internal.instance_type.c6.get_instances_list()) > 0
def test_get_internal_data_instance_type_c6_get():
  assert len(ec2_compare.internal.instance_type.c6.get) > 0
