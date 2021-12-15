
# Testing module instance_type.dl1
import pytest
import ec2_compare.internal.instance_type.dl1

def test_get_internal_data_instance_type_dl1_get_instances_list():
  assert len(ec2_compare.internal.instance_type.dl1.get_instances_list()) > 0
def test_get_internal_data_instance_type_dl1_get():
  assert len(ec2_compare.internal.instance_type.dl1.get) > 0
