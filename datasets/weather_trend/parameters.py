from typing import Sequence
import squirrels as sr

from datasets import common as c

def main(*args, **kwargs) -> Sequence[sr.Parameter]:
    return [c.trend_type_parameter, c.filter_by_parameter, c.time_period_parameter]
