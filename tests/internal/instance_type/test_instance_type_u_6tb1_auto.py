
# Testing module instance_type.u_6tb1
import pytest
import ec2_compare.internal.instance_type.u_6tb1

def test_get_internal_data_instance_type_u_6tb1_get_instances_list():
  assert len(ec2_compare.internal.instance_type.u_6tb1.get_instances_list()) > 0
def test_get_internal_data_instance_type_u_6tb1_get():
  assert len(ec2_compare.internal.instance_type.u_6tb1.get) > 0
