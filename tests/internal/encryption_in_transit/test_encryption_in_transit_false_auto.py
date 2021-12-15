
# Testing module encryption_in_transit.false
import pytest
import ec2_compare.internal.encryption_in_transit.false

def test_get_internal_data_encryption_in_transit_false_get_instances_list():
  assert len(ec2_compare.internal.encryption_in_transit.false.get_instances_list()) > 0
def test_get_internal_data_encryption_in_transit_false_get():
  assert len(ec2_compare.internal.encryption_in_transit.false.get) > 0
