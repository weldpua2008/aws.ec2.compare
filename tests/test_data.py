import pytest
import ec2_compare.data

def test_get():
    for _fixture in zip(
            [
                "InstanceType", "InstanceType", "InstanceType"
            ],
            [
                "i3", "a1", "a"
            ]):
        assert len(ec2_compare.data.get(
            key=_fixture[0],
            value=_fixture[1]

        )) > 0
