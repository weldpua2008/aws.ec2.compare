
# Testing module ipv6.true
import pytest
import ec2_compare.internal.ipv6.true

def test_get_internal_data_ipv6_true_get_instances_list():
  assert len(ec2_compare.internal.ipv6.true.get_instances_list()) > 0
def test_get_internal_data_ipv6_true_get():
  assert len(ec2_compare.internal.ipv6.true.get) > 0
