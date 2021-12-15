
# Testing module instance_type.g4ad
import pytest
import ec2_compare.internal.instance_type.g4ad

def test_get_internal_data_instance_type_g4ad_get_instances_list():
  assert len(ec2_compare.internal.instance_type.g4ad.get_instances_list()) > 0
def test_get_internal_data_instance_type_g4ad_get():
  assert len(ec2_compare.internal.instance_type.g4ad.get) > 0
