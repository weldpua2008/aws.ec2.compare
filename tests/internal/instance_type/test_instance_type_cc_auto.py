
# Testing module instance_type.cc
import pytest
import ec2_compare.internal.instance_type.cc

def test_get_internal_data_instance_type_cc_get_instances_list():
  assert len(ec2_compare.internal.instance_type.cc.get_instances_list()) > 0
def test_get_internal_data_instance_type_cc_get():
  assert len(ec2_compare.internal.instance_type.cc.get) > 0
