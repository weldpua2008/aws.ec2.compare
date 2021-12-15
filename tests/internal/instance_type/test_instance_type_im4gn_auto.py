
# Testing module instance_type.im4gn
import pytest
import ec2_compare.internal.instance_type.im4gn

def test_get_internal_data_instance_type_im4gn_get_instances_list():
  assert len(ec2_compare.internal.instance_type.im4gn.get_instances_list()) > 0
def test_get_internal_data_instance_type_im4gn_get():
  assert len(ec2_compare.internal.instance_type.im4gn.get) > 0
