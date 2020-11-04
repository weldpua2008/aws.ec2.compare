
# Testing module current_generation.false
import pytest
import ec2_compare.internal.current_generation.false

def test_get_internal_data_current_generation_false_get_instances_list():
  assert len(ec2_compare.internal.current_generation.false.get_instances_list()) > 0
def test_get_internal_data_current_generation_false_get():
  assert len(ec2_compare.internal.current_generation.false.get) > 0
