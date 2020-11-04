
# Testing module instance_type.m5n
import pytest
import ec2_compare.internal.instance_type.m5n

def test_get_internal_data_instance_type_m5n_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m5n.get_instances_list()) > 0
def test_get_internal_data_instance_type_m5n_get():
  assert len(ec2_compare.internal.instance_type.m5n.get) > 0
