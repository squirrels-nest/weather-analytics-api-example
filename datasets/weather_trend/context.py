from typing import Dict, Any
import squirrels as sr


def main(prms: Dict[str, sr.Parameter], args: Dict[str, Any], *p_args, **kwargs) -> Dict[str, Any]:
    group_by_param: sr.SingleSelectParameter = prms['trend_type']
    filter_by_param: sr.SingleSelectParameter = prms['filter_by']
    time_period_param: sr.MultiSelectParameter = prms['time_period']
    time_periods_joined = time_period_param.get_selected_labels_quoted_joined()

    return {
        'dim_col': group_by_param.get_selected("dim_col"),
        'alias': group_by_param.get_selected("alias"),
        'filter_by_col': filter_by_param.get_selected("column"),
        'time_periods': time_periods_joined
    }
