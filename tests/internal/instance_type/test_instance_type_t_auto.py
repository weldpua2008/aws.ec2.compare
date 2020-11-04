
# Testing module instance_type.t
import pytest
import ec2_compare.internal.instance_type.t

def test_get_internal_data_instance_type_t_get_instances_list():
  assert len(ec2_compare.internal.instance_type.t.get_instances_list()) > 0
def test_get_internal_data_instance_type_t_get():
  assert len(ec2_compare.internal.instance_type.t.get) > 0
