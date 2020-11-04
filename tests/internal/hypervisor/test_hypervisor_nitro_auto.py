
# Testing module hypervisor.nitro
import pytest
import ec2_compare.internal.hypervisor.nitro

def test_get_internal_data_hypervisor_nitro_get_instances_list():
  assert len(ec2_compare.internal.hypervisor.nitro.get_instances_list()) > 0
def test_get_internal_data_hypervisor_nitro_get():
  assert len(ec2_compare.internal.hypervisor.nitro.get) > 0
