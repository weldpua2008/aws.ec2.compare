
# Testing module instance_type.x2gd
import pytest
import ec2_compare.internal.instance_type.x2gd

def test_get_internal_data_instance_type_x2gd_get_instances_list():
  assert len(ec2_compare.internal.instance_type.x2gd.get_instances_list()) > 0
def test_get_internal_data_instance_type_x2gd_get():
  assert len(ec2_compare.internal.instance_type.x2gd.get) > 0
