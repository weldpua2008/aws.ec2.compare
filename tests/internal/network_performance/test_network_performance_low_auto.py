
# Testing module network_performance.low
import pytest
import ec2_compare.internal.network_performance.low

def test_get_internal_data_network_performance_low_get_instances_list():
  assert len(ec2_compare.internal.network_performance.low.get_instances_list()) > 0
def test_get_internal_data_network_performance_low_get():
  assert len(ec2_compare.internal.network_performance.low.get) > 0
