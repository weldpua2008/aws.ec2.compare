
# Testing module ipv6.false
import pytest
import ec2_compare.internal.ipv6.false

def test_get_internal_data_ipv6_false_get_instances_list():
  assert len(ec2_compare.internal.ipv6.false.get_instances_list()) > 0
def test_get_internal_data_ipv6_false_get():
  assert len(ec2_compare.internal.ipv6.false.get) > 0
