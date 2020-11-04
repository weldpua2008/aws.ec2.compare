
# Testing module instance_type.c6gd
import pytest
import ec2_compare.internal.instance_type.c6gd

def test_get_internal_data_instance_type_c6gd_get_instances_list():
  assert len(ec2_compare.internal.instance_type.c6gd.get_instances_list()) > 0
def test_get_internal_data_instance_type_c6gd_get():
  assert len(ec2_compare.internal.instance_type.c6gd.get) > 0
