
# Testing module instance_type.c5ad
import pytest
import ec2_compare.internal.instance_type.c5ad

def test_get_internal_data_instance_type_c5ad_get_instances_list():
  assert len(ec2_compare.internal.instance_type.c5ad.get_instances_list()) > 0
def test_get_internal_data_instance_type_c5ad_get():
  assert len(ec2_compare.internal.instance_type.c5ad.get) > 0
