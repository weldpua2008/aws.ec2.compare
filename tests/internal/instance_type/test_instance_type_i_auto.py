
# Testing module instance_type.i
import pytest
import ec2_compare.internal.instance_type.i

def test_get_internal_data_instance_type_i_get_instances_list():
  assert len(ec2_compare.internal.instance_type.i.get_instances_list()) > 0
def test_get_internal_data_instance_type_i_get():
  assert len(ec2_compare.internal.instance_type.i.get) > 0
