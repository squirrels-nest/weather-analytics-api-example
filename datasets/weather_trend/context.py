from typing import Dict, Any
from datasets.parameter_options import TrendTypeOption, FilterByOption
import squirrels as sq


def get_selected_trend_type(prms: sq.ParameterSet) -> TrendTypeOption:
    group_by_param: sq.SingleSelectParameter = prms['trend_type']
    return group_by_param.get_selected()


def get_filter_by_column(prms: sq.ParameterSet) -> str:
    filter_by_param: sq.SingleSelectParameter = prms['filter_by']
    filter_by_option: FilterByOption = filter_by_param.get_selected()
    return filter_by_option.column


def get_time_periods(prms: sq.ParameterSet) -> str:
    time_period_param: sq.MultiSelectParameter = prms['time_period']
    return time_period_param.get_selected_labels_quoted_joined()


def main(prms: sq.ParameterSet, proj: Dict[str, str], *args, **kwargs) -> Dict[str, Any]:
    trend_type_option = get_selected_trend_type(prms)

    return {
        'dim_col': trend_type_option.dim_col,
        'alias': trend_type_option.alias,
        'filter_by_col': get_filter_by_column(prms),
        'time_periods': get_time_periods(prms)
    }