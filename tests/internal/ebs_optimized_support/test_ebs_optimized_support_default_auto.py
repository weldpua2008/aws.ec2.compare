
# Testing module ebs_optimized_support.default
import pytest
import ec2_compare.internal.ebs_optimized_support.default

def test_get_internal_data_ebs_optimized_support_default_get_instances_list():
  assert len(ec2_compare.internal.ebs_optimized_support.default.get_instances_list()) > 0
def test_get_internal_data_ebs_optimized_support_default_get():
  assert len(ec2_compare.internal.ebs_optimized_support.default.get) > 0
