
# Testing module auto_recovery.false
import pytest
import ec2_compare.internal.auto_recovery.false

def test_get_internal_data_auto_recovery_false_get_instances_list():
  assert len(ec2_compare.internal.auto_recovery.false.get_instances_list()) > 0
def test_get_internal_data_auto_recovery_false_get():
  assert len(ec2_compare.internal.auto_recovery.false.get) > 0
