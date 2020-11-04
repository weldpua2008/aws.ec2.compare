
# Testing module root_device.instance_store
import pytest
import ec2_compare.internal.root_device.instance_store

def test_get_internal_data_root_device_instance_store_get_instances_list():
  assert len(ec2_compare.internal.root_device.instance_store.get_instances_list()) > 0
def test_get_internal_data_root_device_instance_store_get():
  assert len(ec2_compare.internal.root_device.instance_store.get) > 0
