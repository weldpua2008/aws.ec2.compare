import json
from pathlib import Path

with open(Path(__file__).resolve().parent / "aws_ec2.json") as json_file:
    with open(Path(Path(__file__).resolve().parent).parent / "ec2_compare/ec2data.py",'w') as outfile:
        outfile.write("def get_instances_dict() -> list:\n")
        outfile.write('    # pylint: disable=all\n')
        outfile.write('    return {} # noqa: E501\n'.format(json.load(json_file)) )
