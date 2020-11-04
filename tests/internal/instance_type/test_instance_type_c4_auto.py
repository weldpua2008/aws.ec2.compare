
# Testing module instance_type.c4
import pytest
import ec2_compare.internal.instance_type.c4

def test_get_internal_data_instance_type_c4_get_instances_list():
  assert len(ec2_compare.internal.instance_type.c4.get_instances_list()) > 0
def test_get_internal_data_instance_type_c4_get():
  assert len(ec2_compare.internal.instance_type.c4.get) > 0
