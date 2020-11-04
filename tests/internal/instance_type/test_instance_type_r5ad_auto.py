
# Testing module instance_type.r5ad
import pytest
import ec2_compare.internal.instance_type.r5ad

def test_get_internal_data_instance_type_r5ad_get_instances_list():
  assert len(ec2_compare.internal.instance_type.r5ad.get_instances_list()) > 0
def test_get_internal_data_instance_type_r5ad_get():
  assert len(ec2_compare.internal.instance_type.r5ad.get) > 0
