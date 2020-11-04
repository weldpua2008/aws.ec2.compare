
# Testing module hibernation.true
import pytest
import ec2_compare.internal.hibernation.true

def test_get_internal_data_hibernation_true_get_instances_list():
  assert len(ec2_compare.internal.hibernation.true.get_instances_list()) > 0
def test_get_internal_data_hibernation_true_get():
  assert len(ec2_compare.internal.hibernation.true.get) > 0
