
# Testing module instance_type.c6gn
import pytest
import ec2_compare.internal.instance_type.c6gn

def test_get_internal_data_instance_type_c6gn_get_instances_list():
  assert len(ec2_compare.internal.instance_type.c6gn.get_instances_list()) > 0
def test_get_internal_data_instance_type_c6gn_get():
  assert len(ec2_compare.internal.instance_type.c6gn.get) > 0
