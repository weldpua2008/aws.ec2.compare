
# Testing module strategies.cluster
import pytest
import ec2_compare.internal.strategies.cluster

def test_get_internal_data_strategies_cluster_get_instances_list():
  assert len(ec2_compare.internal.strategies.cluster.get_instances_list()) > 0
def test_get_internal_data_strategies_cluster_get():
  assert len(ec2_compare.internal.strategies.cluster.get) > 0
