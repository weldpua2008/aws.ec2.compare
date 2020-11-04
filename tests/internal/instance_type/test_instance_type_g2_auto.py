
# Testing module instance_type.g2
import pytest
import ec2_compare.internal.instance_type.g2

def test_get_internal_data_instance_type_g2_get_instances_list():
  assert len(ec2_compare.internal.instance_type.g2.get_instances_list()) > 0
def test_get_internal_data_instance_type_g2_get():
  assert len(ec2_compare.internal.instance_type.g2.get) > 0
