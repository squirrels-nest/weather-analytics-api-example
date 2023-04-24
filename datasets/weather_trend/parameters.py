from datasets.parameter_options import trend_type_options, filter_by_options, time_period_options
import squirrels as sq


def main(*args, **kwargs) -> sq.ParameterSet:
    trend_type_parameter = sq.SingleSelectParameter('trend_type', 'Trend Type', trend_type_options)
    filter_by_parameter = sq.SingleSelectParameter('filter_by', 'Filter Time Period By', filter_by_options)
    time_period_parameter = sq.DataSourceParameter(sq.WidgetType.MultiSelect, 'time_period', 'Time Period of', 
                                                   time_period_options, parent=filter_by_parameter)

    return sq.ParameterSet([trend_type_parameter, filter_by_parameter, time_period_parameter])
