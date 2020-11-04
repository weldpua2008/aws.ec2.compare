
# Testing module instance_type.p
import pytest
import ec2_compare.internal.instance_type.p

def test_get_internal_data_instance_type_p_get_instances_list():
  assert len(ec2_compare.internal.instance_type.p.get_instances_list()) > 0
def test_get_internal_data_instance_type_p_get():
  assert len(ec2_compare.internal.instance_type.p.get) > 0
