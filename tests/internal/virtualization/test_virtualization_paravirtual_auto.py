
# Testing module virtualization.paravirtual
import pytest
import ec2_compare.internal.virtualization.paravirtual

def test_get_internal_data_virtualization_paravirtual_get_instances_list():
  assert len(ec2_compare.internal.virtualization.paravirtual.get_instances_list()) > 0
def test_get_internal_data_virtualization_paravirtual_get():
  assert len(ec2_compare.internal.virtualization.paravirtual.get) > 0
