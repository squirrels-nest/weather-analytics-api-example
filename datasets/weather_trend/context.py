from typing import Dict, Any
import squirrels as sr

from datasets.common import TrendTypeOption, FilterByOption


def main(prms: Dict[str, sr.Parameter], args: Dict[str, Any], *p_args, **kwargs) -> Dict[str, Any]:
    group_by_param: sr.SingleSelectParameter = prms['trend_type']
    trend_type_option: TrendTypeOption = group_by_param.get_selected()

    filter_by_param: sr.SingleSelectParameter = prms['filter_by']
    filter_by_option: FilterByOption = filter_by_param.get_selected()

    time_period_param: sr.MultiSelectParameter = prms['time_period']
    time_periods_joined = time_period_param.get_selected_labels_quoted_joined()

    return {
        'dim_col': trend_type_option.dim_col,
        'alias': trend_type_option.alias,
        'filter_by_col': filter_by_option.column,
        'time_periods': time_periods_joined
    }
