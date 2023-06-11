from typing import Dict, Any
import squirrels as sr

from datasets.common import GroupByOption


def main(prms: Dict[str, sr.Parameter], args: Dict[str, Any], *p_args, **kwargs) -> Dict[str, Any]:
    group_by_param: sr.SingleSelectParameter = prms['group_by']
    group_by_option: GroupByOption = group_by_param.get_selected()

    return {
        'dim_col': group_by_option.dim_col,
        'order_col': group_by_option.order_by_col
    }
