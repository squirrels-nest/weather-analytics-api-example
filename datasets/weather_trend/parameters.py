from typing import Sequence
import squirrels as sr

from datasets import common_params as cp

def main(*args, **kwargs) -> Sequence[sr.Parameter]:
    return [cp.trend_type_parameter, cp.filter_by_parameter, cp.time_period_parameter]
