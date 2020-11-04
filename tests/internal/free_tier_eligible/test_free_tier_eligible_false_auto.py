
# Testing module free_tier_eligible.false
import pytest
import ec2_compare.internal.free_tier_eligible.false

def test_get_internal_data_free_tier_eligible_false_get_instances_list():
  assert len(ec2_compare.internal.free_tier_eligible.false.get_instances_list()) > 0
def test_get_internal_data_free_tier_eligible_false_get():
  assert len(ec2_compare.internal.free_tier_eligible.false.get) > 0
