
# Testing module hibernation.false
import pytest
import ec2_compare.internal.hibernation.false

def test_get_internal_data_hibernation_false_get_instances_list():
  assert len(ec2_compare.internal.hibernation.false.get_instances_list()) > 0
def test_get_internal_data_hibernation_false_get():
  assert len(ec2_compare.internal.hibernation.false.get) > 0
