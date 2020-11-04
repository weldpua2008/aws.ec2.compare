
# Testing module instance_type.inf1
import pytest
import ec2_compare.internal.instance_type.inf1

def test_get_internal_data_instance_type_inf1_get_instances_list():
  assert len(ec2_compare.internal.instance_type.inf1.get_instances_list()) > 0
def test_get_internal_data_instance_type_inf1_get():
  assert len(ec2_compare.internal.instance_type.inf1.get) > 0
