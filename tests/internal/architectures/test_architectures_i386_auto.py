
# Testing module architectures.i386
import pytest
import ec2_compare.internal.architectures.i386

def test_get_internal_data_architectures_i386_get_instances_list():
  assert len(ec2_compare.internal.architectures.i386.get_instances_list()) > 0
def test_get_internal_data_architectures_i386_get():
  assert len(ec2_compare.internal.architectures.i386.get) > 0
