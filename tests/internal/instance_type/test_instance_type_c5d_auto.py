
# Testing module instance_type.c5d
import pytest
import ec2_compare.internal.instance_type.c5d

def test_get_internal_data_instance_type_c5d_get_instances_list():
  assert len(ec2_compare.internal.instance_type.c5d.get_instances_list()) > 0
def test_get_internal_data_instance_type_c5d_get():
  assert len(ec2_compare.internal.instance_type.c5d.get) > 0
