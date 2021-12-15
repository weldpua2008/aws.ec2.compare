
# Testing module instance_type.is4gen
import pytest
import ec2_compare.internal.instance_type.is4gen

def test_get_internal_data_instance_type_is4gen_get_instances_list():
  assert len(ec2_compare.internal.instance_type.is4gen.get_instances_list()) > 0
def test_get_internal_data_instance_type_is4gen_get():
  assert len(ec2_compare.internal.instance_type.is4gen.get) > 0
