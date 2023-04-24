from datasets.parameter_options import group_by_options
import squirrels as sq


def main(*args, **kwargs) -> sq.ParameterSet:
    return sq.ParameterSet([
        sq.SingleSelectParameter('group_by', 'Group By', group_by_options),
    ])
