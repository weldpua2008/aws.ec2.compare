
# Testing module network_performance.moderate
import pytest
import ec2_compare.internal.network_performance.moderate

def test_get_internal_data_network_performance_moderate_get_instances_list():
  assert len(ec2_compare.internal.network_performance.moderate.get_instances_list()) > 0
def test_get_internal_data_network_performance_moderate_get():
  assert len(ec2_compare.internal.network_performance.moderate.get) > 0
