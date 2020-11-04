
# Testing module burstable_performance.true
import pytest
import ec2_compare.internal.burstable_performance.true

def test_get_internal_data_burstable_performance_true_get_instances_list():
  assert len(ec2_compare.internal.burstable_performance.true.get_instances_list()) > 0
def test_get_internal_data_burstable_performance_true_get():
  assert len(ec2_compare.internal.burstable_performance.true.get) > 0
