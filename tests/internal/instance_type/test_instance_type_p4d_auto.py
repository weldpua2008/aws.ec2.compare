
# Testing module instance_type.p4d
import pytest
import ec2_compare.internal.instance_type.p4d

def test_get_internal_data_instance_type_p4d_get_instances_list():
  assert len(ec2_compare.internal.instance_type.p4d.get_instances_list()) > 0
def test_get_internal_data_instance_type_p4d_get():
  assert len(ec2_compare.internal.instance_type.p4d.get) > 0
