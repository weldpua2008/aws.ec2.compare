
# Testing module instance_type.f
import pytest
import ec2_compare.internal.instance_type.f

def test_get_internal_data_instance_type_f_get_instances_list():
  assert len(ec2_compare.internal.instance_type.f.get_instances_list()) > 0
def test_get_internal_data_instance_type_f_get():
  assert len(ec2_compare.internal.instance_type.f.get) > 0
