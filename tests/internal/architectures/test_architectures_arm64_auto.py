
# Testing module architectures.arm64
import pytest
import ec2_compare.internal.architectures.arm64

def test_get_internal_data_architectures_arm64_get_instances_list():
  assert len(ec2_compare.internal.architectures.arm64.get_instances_list()) > 0
def test_get_internal_data_architectures_arm64_get():
  assert len(ec2_compare.internal.architectures.arm64.get) > 0
