
# Testing module instance_type.r5dn
import pytest
import ec2_compare.internal.instance_type.r5dn

def test_get_internal_data_instance_type_r5dn_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r5dn.get_instances_list()) > 0
def test_get_internal_data_instance_type_r5dn_get():
  assert len(ec2_compare.internal.instance_type.r5dn.get) > 0
