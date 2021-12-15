
# Testing module efa.true
import pytest
import ec2_compare.internal.efa.true

def test_get_internal_data_efa_true_get_instances_list():
  assert len(ec2_compare.internal.efa.true.get_instances_list()) > 0
def test_get_internal_data_efa_true_get():
  assert len(ec2_compare.internal.efa.true.get) > 0
