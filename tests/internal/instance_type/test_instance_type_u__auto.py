
# Testing module instance_type.u_
import pytest
import ec2_compare.internal.instance_type.u_

def test_get_internal_data_instance_type_u__get_instances_list():
  assert len(ec2_compare.internal.instance_type.u_.get_instances_list()) > 0
def test_get_internal_data_instance_type_u__get():
  assert len(ec2_compare.internal.instance_type.u_.get) > 0
