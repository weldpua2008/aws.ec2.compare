
# Testing module burstable_performance.false
import pytest
import ec2_compare.internal.burstable_performance.false

def test_get_internal_data_burstable_performance_false_get_instances_list():
  assert len(ec2_compare.internal.burstable_performance.false.get_instances_list()) > 0
def test_get_internal_data_burstable_performance_false_get():
  assert len(ec2_compare.internal.burstable_performance.false.get) > 0
