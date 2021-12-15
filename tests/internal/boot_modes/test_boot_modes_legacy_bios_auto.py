
# Testing module boot_modes.legacy_bios
import pytest
import ec2_compare.internal.boot_modes.legacy_bios

def test_get_internal_data_boot_modes_legacy_bios_get_instances_list():
  assert len(ec2_compare.internal.boot_modes.legacy_bios.get_instances_list()) > 0
def test_get_internal_data_boot_modes_legacy_bios_get():
  assert len(ec2_compare.internal.boot_modes.legacy_bios.get) > 0
