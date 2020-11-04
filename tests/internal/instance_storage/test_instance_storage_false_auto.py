
# Testing module instance_storage.false
import pytest
import ec2_compare.internal.instance_storage.false

def test_get_internal_data_instance_storage_false_get_instances_list():
  assert len(ec2_compare.internal.instance_storage.false.get_instances_list()) > 0
def test_get_internal_data_instance_storage_false_get():
  assert len(ec2_compare.internal.instance_storage.false.get) > 0
