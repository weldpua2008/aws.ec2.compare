
# Testing module usage_classes.on_demand
import pytest
import ec2_compare.internal.usage_classes.on_demand

def test_get_internal_data_usage_classes_on_demand_get_instances_list():
  assert len(ec2_compare.internal.usage_classes.on_demand.get_instances_list()) > 0
def test_get_internal_data_usage_classes_on_demand_get():
  assert len(ec2_compare.internal.usage_classes.on_demand.get) > 0
