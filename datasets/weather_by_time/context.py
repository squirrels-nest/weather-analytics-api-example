from typing import Dict, Any
from datasets.parameter_options import GroupByOption
import squirrels as sq


def get_selected_group_by(prms: sq.ParameterSet) -> GroupByOption:
    group_by_param: sq.SingleSelectParameter = prms['group_by']
    return group_by_param.get_selected()


def main(prms: sq.ParameterSet, proj: Dict[str, str], *args, **kwargs) -> Dict[str, Any]:
    group_by_option = get_selected_group_by(prms)

    return {
        'dim_col': group_by_option.dim_col,
        'order_col': group_by_option.order_by_col
    }