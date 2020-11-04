
# Testing module root_device.ebs
import pytest
import ec2_compare.internal.root_device.ebs

def test_get_internal_data_root_device_ebs_get_instances_list():
  assert len(ec2_compare.internal.root_device.ebs.get_instances_list()) > 0
def test_get_internal_data_root_device_ebs_get():
  assert len(ec2_compare.internal.root_device.ebs.get) > 0
