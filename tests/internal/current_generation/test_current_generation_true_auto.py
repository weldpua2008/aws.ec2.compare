
# Testing module current_generation.true
import pytest
import ec2_compare.internal.current_generation.true

def test_get_internal_data_current_generation_true_get_instances_list():
  assert len(ec2_compare.internal.current_generation.true.get_instances_list()) > 0
def test_get_internal_data_current_generation_true_get():
  assert len(ec2_compare.internal.current_generation.true.get) > 0
