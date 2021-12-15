
# Testing module instance_type.vt
import pytest
import ec2_compare.internal.instance_type.vt

def test_get_internal_data_instance_type_vt_get_instances_list():
  assert len(ec2_compare.internal.instance_type.vt.get_instances_list()) > 0
def test_get_internal_data_instance_type_vt_get():
  assert len(ec2_compare.internal.instance_type.vt.get) > 0
