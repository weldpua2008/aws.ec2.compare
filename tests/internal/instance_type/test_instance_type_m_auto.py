
# Testing module instance_type.m
import pytest
import ec2_compare.internal.instance_type.m

def test_get_internal_data_instance_type_m_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m.get_instances_list()) > 0
def test_get_internal_data_instance_type_m_get():
  assert len(ec2_compare.internal.instance_type.m.get) > 0
