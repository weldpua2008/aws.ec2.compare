
# Testing module virtualization.hvm
import pytest
import ec2_compare.internal.virtualization.hvm

def test_get_internal_data_virtualization_hvm_get_instances_list():
  assert len(ec2_compare.internal.virtualization.hvm.get_instances_list()) > 0
def test_get_internal_data_virtualization_hvm_get():
  assert len(ec2_compare.internal.virtualization.hvm.get) > 0
