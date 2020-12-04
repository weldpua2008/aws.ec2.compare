
# Testing module encryption_support.unsupported
import pytest
import ec2_compare.internal.encryption_support.unsupported

def test_get_internal_data_encryption_support_unsupported_get_instances_list():
  assert len(ec2_compare.internal.encryption_support.unsupported.get_instances_list()) > 0
def test_get_internal_data_encryption_support_unsupported_get():
  assert len(ec2_compare.internal.encryption_support.unsupported.get) > 0
