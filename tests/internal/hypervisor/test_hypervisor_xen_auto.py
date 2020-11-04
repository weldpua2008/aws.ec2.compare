
# Testing module hypervisor.xen
import pytest
import ec2_compare.internal.hypervisor.xen

def test_get_internal_data_hypervisor_xen_get_instances_list():
  assert len(ec2_compare.internal.hypervisor.xen.get_instances_list()) > 0
def test_get_internal_data_hypervisor_xen_get():
  assert len(ec2_compare.internal.hypervisor.xen.get) > 0
