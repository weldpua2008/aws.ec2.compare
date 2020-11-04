
# Testing module bare_metal.false
import pytest
import ec2_compare.internal.bare_metal.false

def test_get_internal_data_bare_metal_false_get_instances_list():
  assert len(ec2_compare.internal.bare_metal.false.get_instances_list()) > 0
def test_get_internal_data_bare_metal_false_get():
  assert len(ec2_compare.internal.bare_metal.false.get) > 0
