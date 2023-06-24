from typing import Dict, Any
import squirrels as sr


def main(prms: Dict[str, sr.Parameter], args: Dict[str, Any], *p_args, **kwargs) -> Dict[str, Any]:
    group_by_param: sr.SingleSelectParameter = prms['group_by']
    group_by_option = group_by_param.get_selected()
    dim_col = group_by_option.custom_fields["dim_col"]
    order_by_col = group_by_option.custom_fields.get("order_by_col", dim_col)

    return {
        'dim_col': dim_col,
        'order_col': order_by_col
    }
