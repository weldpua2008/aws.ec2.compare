
# Testing module ena_support.required
import pytest
import ec2_compare.internal.ena_support.required

def test_get_internal_data_ena_support_required_get_instances_list():
  assert len(ec2_compare.internal.ena_support.required.get_instances_list()) > 0
def test_get_internal_data_ena_support_required_get():
  assert len(ec2_compare.internal.ena_support.required.get) > 0
