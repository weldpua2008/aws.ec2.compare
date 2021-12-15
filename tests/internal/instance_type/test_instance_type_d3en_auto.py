
# Testing module instance_type.d3en
import pytest
import ec2_compare.internal.instance_type.d3en

def test_get_internal_data_instance_type_d3en_get_instances_list():
  assert len(ec2_compare.internal.instance_type.d3en.get_instances_list()) > 0
def test_get_internal_data_instance_type_d3en_get():
  assert len(ec2_compare.internal.instance_type.d3en.get) > 0
