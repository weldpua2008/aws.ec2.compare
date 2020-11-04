
# Testing module instance_type.inf
import pytest
import ec2_compare.internal.instance_type.inf

def test_get_internal_data_instance_type_inf_get_instances_list():
  assert len(ec2_compare.internal.instance_type.inf.get_instances_list()) > 0
def test_get_internal_data_instance_type_inf_get():
  assert len(ec2_compare.internal.instance_type.inf.get) > 0
