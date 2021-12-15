
# Testing module instance_type.im
import pytest
import ec2_compare.internal.instance_type.im

def test_get_internal_data_instance_type_im_get_instances_list():
  assert len(ec2_compare.internal.instance_type.im.get_instances_list()) > 0
def test_get_internal_data_instance_type_im_get():
  assert len(ec2_compare.internal.instance_type.im.get) > 0
