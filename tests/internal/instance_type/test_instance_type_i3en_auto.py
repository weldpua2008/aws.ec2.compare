
# Testing module instance_type.i3en
import pytest
import ec2_compare.internal.instance_type.i3en

def test_get_internal_data_instance_type_i3en_get_instances_list():
  assert len(ec2_compare.internal.instance_type.i3en.get_instances_list()) > 0
def test_get_internal_data_instance_type_i3en_get():
  assert len(ec2_compare.internal.instance_type.i3en.get) > 0
