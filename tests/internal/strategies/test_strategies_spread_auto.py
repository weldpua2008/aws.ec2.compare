
# Testing module strategies.spread
import pytest
import ec2_compare.internal.strategies.spread

def test_get_internal_data_strategies_spread_get_instances_list():
  assert len(ec2_compare.internal.strategies.spread.get_instances_list()) > 0
def test_get_internal_data_strategies_spread_get():
  assert len(ec2_compare.internal.strategies.spread.get) > 0
