
# Testing module instance_type.c5
import pytest
import ec2_compare.internal.instance_type.c5

def test_get_internal_data_instance_type_c5_get_instances_list():
  assert len(ec2_compare.internal.instance_type.c5.get_instances_list()) > 0
def test_get_internal_data_instance_type_c5_get():
  assert len(ec2_compare.internal.instance_type.c5.get) > 0
