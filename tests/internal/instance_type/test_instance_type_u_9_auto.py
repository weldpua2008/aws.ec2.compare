
# Testing module instance_type.u_9
import pytest
import ec2_compare.internal.instance_type.u_9

def test_get_internal_data_instance_type_u_9_get_instances_list():
  assert len(ec2_compare.internal.instance_type.u_9.get_instances_list()) > 0
def test_get_internal_data_instance_type_u_9_get():
  assert len(ec2_compare.internal.instance_type.u_9.get) > 0
