
# Testing module instance_type.m5d
import pytest
import ec2_compare.internal.instance_type.m5d

def test_get_internal_data_instance_type_m5d_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m5d.get_instances_list()) > 0
def test_get_internal_data_instance_type_m5d_get():
  assert len(ec2_compare.internal.instance_type.m5d.get) > 0
