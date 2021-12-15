
# Testing module instance_type.d3
import pytest
import ec2_compare.internal.instance_type.d3

def test_get_internal_data_instance_type_d3_get_instances_list():
  assert len(ec2_compare.internal.instance_type.d3.get_instances_list()) > 0
def test_get_internal_data_instance_type_d3_get():
  assert len(ec2_compare.internal.instance_type.d3.get) > 0
