
# Testing module instance_type.m6i
import pytest
import ec2_compare.internal.instance_type.m6i

def test_get_internal_data_instance_type_m6i_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m6i.get_instances_list()) > 0
def test_get_internal_data_instance_type_m6i_get():
  assert len(ec2_compare.internal.instance_type.m6i.get) > 0
