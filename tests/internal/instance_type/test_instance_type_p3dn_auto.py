
# Testing module instance_type.p3dn
import pytest
import ec2_compare.internal.instance_type.p3dn

def test_get_internal_data_instance_type_p3dn_get_instances_list():
  assert len(ec2_compare.internal.instance_type.p3dn.get_instances_list()) > 0
def test_get_internal_data_instance_type_p3dn_get():
  assert len(ec2_compare.internal.instance_type.p3dn.get) > 0
