
# Testing module dedicated_hosts.false
import pytest
import ec2_compare.internal.dedicated_hosts.false

def test_get_internal_data_dedicated_hosts_false_get_instances_list():
  assert len(ec2_compare.internal.dedicated_hosts.false.get_instances_list()) > 0
def test_get_internal_data_dedicated_hosts_false_get():
  assert len(ec2_compare.internal.dedicated_hosts.false.get) > 0
