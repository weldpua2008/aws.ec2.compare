
# Testing module strategies.partition
import pytest
import ec2_compare.internal.strategies.partition

def test_get_internal_data_strategies_partition_get_instances_list():
  assert len(ec2_compare.internal.strategies.partition.get_instances_list()) > 0
def test_get_internal_data_strategies_partition_get():
  assert len(ec2_compare.internal.strategies.partition.get) > 0
