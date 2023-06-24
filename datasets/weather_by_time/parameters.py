from typing import Sequence, Dict, Any
import squirrels as sr

from datasets import common_params as cp


def main(args: Dict[str, Any], *p_args, **kwargs) -> Sequence[sr.Parameter]:
    return [cp.group_by_param]
