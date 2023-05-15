import squirrels as sq

from datasets import common as c

def main(*args, **kwargs) -> sq.ParameterSet:
    return sq.ParameterSet([c.trend_type_parameter, c.filter_by_parameter, c.time_period_parameter])
