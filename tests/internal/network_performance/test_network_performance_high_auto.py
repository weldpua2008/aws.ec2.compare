
# Testing module network_performance.high
import pytest
import ec2_compare.internal.network_performance.high

def test_get_internal_data_network_performance_high_get_instances_list():
  assert len(ec2_compare.internal.network_performance.high.get_instances_list()) > 0
def test_get_internal_data_network_performance_high_get():
  assert len(ec2_compare.internal.network_performance.high.get) > 0
