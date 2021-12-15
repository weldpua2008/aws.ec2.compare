
# Testing module instance_type.r6i
import pytest
import ec2_compare.internal.instance_type.r6i

def test_get_internal_data_instance_type_r6i_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r6i.get_instances_list()) > 0
def test_get_internal_data_instance_type_r6i_get():
  assert len(ec2_compare.internal.instance_type.r6i.get) > 0
