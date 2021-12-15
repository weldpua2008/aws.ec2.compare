
# Testing module nvme_support.required
import pytest
import ec2_compare.internal.nvme_support.required

def test_get_internal_data_nvme_support_required_get_instances_list():
  assert len(ec2_compare.internal.nvme_support.required.get_instances_list()) > 0
def test_get_internal_data_nvme_support_required_get():
  assert len(ec2_compare.internal.nvme_support.required.get) > 0
