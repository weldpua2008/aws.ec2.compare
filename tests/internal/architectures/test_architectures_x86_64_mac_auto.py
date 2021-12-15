
# Testing module architectures.x86_64_mac
import pytest
import ec2_compare.internal.architectures.x86_64_mac

def test_get_internal_data_architectures_x86_64_mac_get_instances_list():
  assert len(ec2_compare.internal.architectures.x86_64_mac.get_instances_list()) > 0
def test_get_internal_data_architectures_x86_64_mac_get():
  assert len(ec2_compare.internal.architectures.x86_64_mac.get) > 0
