
# Testing module instance_type.mac
import pytest
import ec2_compare.internal.instance_type.mac

def test_get_internal_data_instance_type_mac_get_instances_list():
  assert len(ec2_compare.internal.instance_type.mac.get_instances_list()) > 0
def test_get_internal_data_instance_type_mac_get():
  assert len(ec2_compare.internal.instance_type.mac.get) > 0
