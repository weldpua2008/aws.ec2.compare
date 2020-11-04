
# Testing module instance_type.h
import pytest
import ec2_compare.internal.instance_type.h

def test_get_internal_data_instance_type_h_get_instances_list():
  assert len(ec2_compare.internal.instance_type.h.get_instances_list()) > 0
def test_get_internal_data_instance_type_h_get():
  assert len(ec2_compare.internal.instance_type.h.get) > 0
