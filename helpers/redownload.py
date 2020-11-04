import json
from pathlib import Path
import textwrap
import itertools
from datetime import date
import re
def getCurrentMemoryUsage():
    ''' Memory usage in Bytes '''
    import psutil
    import os
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

def remove_suffix(value, suffix):
    return value[:-len(suffix)] if value.endswith(suffix) else value

def done(fn, _mem_start):
    print("* {} - used RAM {:.2f} MB of {:.2f} MB Total [ DONE ]".format(
        fn,
        (getCurrentMemoryUsage()-_mem_start) / 1048576 ,
        (getCurrentMemoryUsage()/1048576)
        ))

_parent = Path(__file__).resolve().parent
_package_root = Path( _parent.parent  / "ec2_compare")
_tests_root = Path( _parent.parent  / "tests")
print("Parsing cache file 'aws_ec2.json':")
_mem_start = getCurrentMemoryUsage()

with open(_parent / "aws_ec2.json") as json_file:
    data = json.load(json_file)
    _raw_package_root = Path(_package_root / "internal")

    fn = "ec2data.py"
    with open(_raw_package_root / fn, 'w') as outfile:
        outfile.write(textwrap.dedent("""
        def get_instances_list() -> list:
            # pylint: disable=all
            return {} # noqa: E501
            """ .format(data) ))

        done(fn, _mem_start)


    _prop_name = 'CurrentGeneration'
    _prop_default = False
    set([  n  for k in data for n in k.keys() if isinstance(k[n], bool)  ])

    exclude_keys = ['InstanceType']
    for t in [bool, str, list]:
        for _filtered_key in set([n for k in data for n in k.keys() if isinstance(k[n], t)]):
            # if _filtered_key in exclude_keys:
            #     print(f"Skipping {_filtered_key}")
            #     continue
            val = []
            if t == list:
                val = set([ n for k in data for n in k[_filtered_key] ])
            elif _filtered_key == 'InstanceType':
                val = set([ k.get(_filtered_key).split(".")[0] for k in data if not k.get(_filtered_key, None) is None ])
                _families = set([ str(re.match(r"^(.*?)\d+",k).group(1)) for k in val if re.match(r"^(.*?)\d+",k) ])
                _sub_families = set([ str(re.match(r"^(.*?)\d+",k).group(0)) for k in val if re.match(r"^(.*?)\d+",k) ])
                val = set(list(val) + list(_families) + list(_sub_families) )
            else:
                val = set([ k.get(_filtered_key) for k in data if not k.get(_filtered_key, None) is None ])
            for _filtered_value in val:
                _display_filtered_key = "".join([("_"+i if j> 0 and i.isupper() else i) for j,i in enumerate(_filtered_key.replace("Supported","").replace("Types","").replace("-","_"))]).strip().lower()
                print(f"Filter {_filtered_key}:{_display_filtered_key} - {_filtered_value}")
                if not _display_filtered_key:
                    continue

                _partial = []
                if t == list:
                    _partial = list(filter(lambda x: _filtered_key in x and _filtered_value in x[_filtered_key] ,data))
                elif _filtered_key == 'InstanceType':
                    _partial = list(filter(lambda x: _filtered_key in x and str(x[_filtered_key]).startswith(str(_filtered_value))  ,data))
                else:
                    _partial = list(filter(lambda x: _filtered_key in x and str(_filtered_value) == str(x[_filtered_key]) ,data))

                if not _partial:
                    continue
                _sub_package = Path(_raw_package_root/str(_display_filtered_key).lower())
                _sub_package.mkdir(parents=True, exist_ok=True)
                with open(_sub_package / '__init__.py', 'w') as outfile:
                    outfile.write(textwrap.dedent("""
                    # Automatically generated at {}
                    """ .format(date.today().strftime("%B %d, %Y")) ))

                _sub_tests = Path(_tests_root/ 'internal/{}'.format(str(_display_filtered_key).lower()))
                _sub_tests.mkdir(parents=True, exist_ok=True)
                _usage_class = str(_filtered_value).lower().replace("-","_")
                fn = "{}.py".format(_usage_class)
                with open(_sub_package / fn, 'w') as outfile:
                    if not _partial:
                        raise ValueError(f"usage_class {_usage_class} is empty ")
                    outfile.write(textwrap.dedent("""
                    # Automatically generated

                    # pylint: disable=all
                    get = {} # noqa: E501

                    def get_instances_list() -> list:
                        '''Returns list EC2 instances with {} = {} .'''
                        # pylint: disable=all
                        return get

                    """ .format(_partial, _filtered_key,
                                _filtered_value,
                                ) ))
                __mod_name = ".".join([_display_filtered_key,_usage_class])
                __func_name = __mod_name.replace(".", "-").replace("-", "_")
                with open(_sub_tests / "test_{}_{}_auto.py".format(_display_filtered_key, _usage_class), 'w') as outfile:
                    outfile.write(textwrap.dedent("""
                    # Testing module {module_name}
                    import pytest
                    import ec2_compare.internal.{module_name}

                    def test_get_internal_data_{func_name}_get_instances_list():
                      assert len(ec2_compare.internal.{module_name}.get_instances_list()) > 0
                    def test_get_internal_data_{func_name}_get():
                      assert len(ec2_compare.internal.{module_name}.get) > 0
                        """ .format(module_name=__mod_name,
                                    func_name=__func_name
                            ) ))
                done(fn, _mem_start)

            done(fn, _mem_start)
