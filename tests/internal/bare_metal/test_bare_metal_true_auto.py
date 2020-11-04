
# Testing module bare_metal.true
import pytest
import ec2_compare.internal.bare_metal.true

def test_get_internal_data_bare_metal_true_get_instances_list():
  assert len(ec2_compare.internal.bare_metal.true.get_instances_list()) > 0
def test_get_internal_data_bare_metal_true_get():
  assert len(ec2_compare.internal.bare_metal.true.get) > 0
