
# Testing module boot_modes.uefi
import pytest
import ec2_compare.internal.boot_modes.uefi

def test_get_internal_data_boot_modes_uefi_get_instances_list():
  assert len(ec2_compare.internal.boot_modes.uefi.get_instances_list()) > 0
def test_get_internal_data_boot_modes_uefi_get():
  assert len(ec2_compare.internal.boot_modes.uefi.get) > 0
