from typing import Dict, Any
import squirrels as sq

from datasets import common as c


def main(args: Dict[str, Any], *p_args, **kwargs) -> sq.ParameterSet:
    return sq.ParameterSet([c.group_by_param])
