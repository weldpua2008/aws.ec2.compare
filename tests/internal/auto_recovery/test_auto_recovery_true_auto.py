
# Testing module auto_recovery.true
import pytest
import ec2_compare.internal.auto_recovery.true

def test_get_internal_data_auto_recovery_true_get_instances_list():
  assert len(ec2_compare.internal.auto_recovery.true.get_instances_list()) > 0
def test_get_internal_data_auto_recovery_true_get():
  assert len(ec2_compare.internal.auto_recovery.true.get) > 0
