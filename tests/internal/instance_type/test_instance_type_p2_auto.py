
# Testing module instance_type.p2
import pytest
import ec2_compare.internal.instance_type.p2

def test_get_internal_data_instance_type_p2_get_instances_list():
  assert len(ec2_compare.internal.instance_type.p2.get_instances_list()) > 0
def test_get_internal_data_instance_type_p2_get():
  assert len(ec2_compare.internal.instance_type.p2.get) > 0
