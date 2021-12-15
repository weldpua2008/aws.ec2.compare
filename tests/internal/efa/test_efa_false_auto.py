
# Testing module efa.false
import pytest
import ec2_compare.internal.efa.false

def test_get_internal_data_efa_false_get_instances_list():
  assert len(ec2_compare.internal.efa.false.get_instances_list()) > 0
def test_get_internal_data_efa_false_get():
  assert len(ec2_compare.internal.efa.false.get) > 0
