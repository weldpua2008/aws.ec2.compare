
# Testing module encryption_in_transit.true
import pytest
import ec2_compare.internal.encryption_in_transit.true

def test_get_internal_data_encryption_in_transit_true_get_instances_list():
  assert len(ec2_compare.internal.encryption_in_transit.true.get_instances_list()) > 0
def test_get_internal_data_encryption_in_transit_true_get():
  assert len(ec2_compare.internal.encryption_in_transit.true.get) > 0
