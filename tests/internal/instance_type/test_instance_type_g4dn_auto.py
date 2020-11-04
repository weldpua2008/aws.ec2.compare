
# Testing module instance_type.g4dn
import pytest
import ec2_compare.internal.instance_type.g4dn

def test_get_internal_data_instance_type_g4dn_get_instances_list():
  assert len(ec2_compare.internal.instance_type.g4dn.get_instances_list()) > 0
def test_get_internal_data_instance_type_g4dn_get():
  assert len(ec2_compare.internal.instance_type.g4dn.get) > 0
