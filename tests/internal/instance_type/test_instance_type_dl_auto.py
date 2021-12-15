
# Testing module instance_type.dl
import pytest
import ec2_compare.internal.instance_type.dl

def test_get_internal_data_instance_type_dl_get_instances_list():
  assert len(ec2_compare.internal.instance_type.dl.get_instances_list()) > 0
def test_get_internal_data_instance_type_dl_get():
  assert len(ec2_compare.internal.instance_type.dl.get) > 0
