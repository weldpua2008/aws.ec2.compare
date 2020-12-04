
# Testing module architectures.x86_64
import pytest
import ec2_compare.internal.architectures.x86_64

def test_get_internal_data_architectures_x86_64_get_instances_list():
  assert len(ec2_compare.internal.architectures.x86_64.get_instances_list()) > 0
def test_get_internal_data_architectures_x86_64_get():
  assert len(ec2_compare.internal.architectures.x86_64.get) > 0
