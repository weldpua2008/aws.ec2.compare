
# Testing module encryption_support.supported
import pytest
import ec2_compare.internal.encryption_support.supported

def test_get_internal_data_encryption_support_supported_get_instances_list():
  assert len(ec2_compare.internal.encryption_support.supported.get_instances_list()) > 0
def test_get_internal_data_encryption_support_supported_get():
  assert len(ec2_compare.internal.encryption_support.supported.get) > 0
