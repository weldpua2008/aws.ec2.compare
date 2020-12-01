import pytest
import ec2_compare.utils as utils



data =  {'a': 65, 'A': 66, 'C': 67, 'D': 68}

def test_dict_values_empty():
    assert list(utils.dict_values(data=data, keys=[])) == []
    assert list(utils.dict_values(data=data,keys=set())) == []

def test_dict_values_no_keys():
    assert list(utils.dict_values(data=data, keys=['z','y'])) == []

def test_dict_values_one_key():
    assert list(utils.dict_values(data=data, keys=['a'])) == [data['a']]

def test_dict_values_several_keys():
    assert sorted(list(utils.dict_values(
        data=data, keys=['a', 'A']))) == sorted([data['a'],data['A']])

def test_dict_values_limit():

    assert sorted(list(utils.dict_values(
        data=data, keys=['a', 'A'],
        limit=1))) == sorted([data['a'],data['A']])[:1]

def test_dict_values_default():
    assert list(utils.dict_values(
        data=data, keys=['z','y'],
        default=['A'])) == ['A']
