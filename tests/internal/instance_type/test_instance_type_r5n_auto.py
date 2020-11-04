
# Testing module instance_type.r5n
import pytest
import ec2_compare.internal.instance_type.r5n

def test_get_internal_data_instance_type_r5n_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r5n.get_instances_list()) > 0
def test_get_internal_data_instance_type_r5n_get():
  assert len(ec2_compare.internal.instance_type.r5n.get) > 0
