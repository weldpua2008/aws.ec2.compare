
# Testing module nvme_support.supported
import pytest
import ec2_compare.internal.nvme_support.supported

def test_get_internal_data_nvme_support_supported_get_instances_list():
  assert len(ec2_compare.internal.nvme_support.supported.get_instances_list()) > 0
def test_get_internal_data_nvme_support_supported_get():
  assert len(ec2_compare.internal.nvme_support.supported.get) > 0
