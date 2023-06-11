import squirrels as sr

# Group bys
class GroupByOption(sr.SelectParameterOption):
    def __init__(self, id, label, dim_col, order_by_col = None):
        super().__init__(id, label)
        self.dim_col = dim_col
        self.order_by_col = order_by_col if order_by_col is not None else dim_col

group_by_options = [
    GroupByOption('0', 'Year', 'year'),
    GroupByOption('1', 'Quarter', 'quarter'),
    GroupByOption('2', 'Month', 'month_name', 'month_order'),
    GroupByOption('3', 'Day of Year', 'day_of_year'),
    GroupByOption('4', 'Condition', 'condition')
]


# Trend type
class TrendTypeOption(GroupByOption):
    def __init__(self, id, label, dim_col, alias):
        super().__init__(id, label, dim_col)
        self.alias = alias

trend_type_options = [
    TrendTypeOption('0', 'Weather Over Years', 'start_of_year', 'year'),
    TrendTypeOption('1', 'Weather Over Quarters', 'start_of_quarter', 'quarter_of'),
    TrendTypeOption('2', 'Weather Over Months', 'start_of_month', 'month_of'),
    TrendTypeOption('3', 'Weather Over Weeks', 'start_of_week', 'week_of')
]


# Filter By options
class FilterByOption(sr.SelectParameterOption):
    def __init__(self, id, label, column) -> None:
        super().__init__(id, label)
        self.column = column

filter_by_options = [
    FilterByOption('0', 'Year', 'start_of_year'),
    FilterByOption('1', 'Quarter', 'start_of_quarter'),
    FilterByOption('2', 'Month', 'start_of_month')
]


# Time Period options
time_period_options = sr.SelectionDataSource('time_lookup', 'index', 'start_of_time', parent_id_col='time_type_id')


# Parameters
class GroupByParameter(sr.SingleSelectParameter):
    def __init__(self) -> None:
        super().__init__('group_by', 'Group By', group_by_options)

group_by_param = GroupByParameter()

trend_type_parameter = sr.SingleSelectParameter('trend_type', 'Trend Type', trend_type_options)
filter_by_parameter = sr.SingleSelectParameter('filter_by', 'Filter Time Period By', filter_by_options)
time_period_parameter = sr.DataSourceParameter(sr.MultiSelectParameter, 'time_period', 'Time Period of', 
                                                time_period_options, parent=filter_by_parameter)
