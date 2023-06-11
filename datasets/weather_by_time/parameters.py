from typing import Sequence, Dict, Any
import squirrels as sr

from datasets import common as c


def main(args: Dict[str, Any], *p_args, **kwargs) -> Sequence[sr.Parameter]:
    return [c.group_by_param]
