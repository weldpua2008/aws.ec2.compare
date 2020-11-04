
# Testing module dedicated_hosts.true
import pytest
import ec2_compare.internal.dedicated_hosts.true

def test_get_internal_data_dedicated_hosts_true_get_instances_list():
  assert len(ec2_compare.internal.dedicated_hosts.true.get_instances_list()) > 0
def test_get_internal_data_dedicated_hosts_true_get():
  assert len(ec2_compare.internal.dedicated_hosts.true.get) > 0
