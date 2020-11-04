
# Testing module usage_classes.spot
import pytest
import ec2_compare.internal.usage_classes.spot

def test_get_internal_data_usage_classes_spot_get_instances_list():
  assert len(ec2_compare.internal.usage_classes.spot.get_instances_list()) > 0
def test_get_internal_data_usage_classes_spot_get():
  assert len(ec2_compare.internal.usage_classes.spot.get) > 0
