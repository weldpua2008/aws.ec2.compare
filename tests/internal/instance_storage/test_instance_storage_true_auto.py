
# Testing module instance_storage.true
import pytest
import ec2_compare.internal.instance_storage.true

def test_get_internal_data_instance_storage_true_get_instances_list():
  assert len(ec2_compare.internal.instance_storage.true.get_instances_list()) > 0
def test_get_internal_data_instance_storage_true_get():
  assert len(ec2_compare.internal.instance_storage.true.get) > 0
