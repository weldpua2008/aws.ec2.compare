
# Testing module instance_type.m5dn
import pytest
import ec2_compare.internal.instance_type.m5dn

def test_get_internal_data_instance_type_m5dn_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m5dn.get_instances_list()) > 0
def test_get_internal_data_instance_type_m5dn_get():
  assert len(ec2_compare.internal.instance_type.m5dn.get) > 0
