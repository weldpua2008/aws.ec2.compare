
# Testing module free_tier_eligible.true
import pytest
import ec2_compare.internal.free_tier_eligible.true

def test_get_internal_data_free_tier_eligible_true_get_instances_list():
  assert len(ec2_compare.internal.free_tier_eligible.true.get_instances_list()) > 0
def test_get_internal_data_free_tier_eligible_true_get():
  assert len(ec2_compare.internal.free_tier_eligible.true.get) > 0
