import squirrels as sr

# Group bys
group_by_options = [
    sr.SelectParameterOption('0', 'Year', dim_col='year'),
    sr.SelectParameterOption('1', 'Quarter', dim_col='quarter'),
    sr.SelectParameterOption('2', 'Month', dim_col='month_name', order_by_col='month_order'),
    sr.SelectParameterOption('3', 'Day of Year', dim_col='day_of_year'),
    sr.SelectParameterOption('4', 'Condition', dim_col='condition')
]

# Trend type
trend_type_options = [
    sr.SelectParameterOption('0', 'Weather Over Years', dim_col='start_of_year', alias='year'),
    sr.SelectParameterOption('1', 'Weather Over Quarters', dim_col='start_of_quarter', alias='quarter_of'),
    sr.SelectParameterOption('2', 'Weather Over Months', dim_col='start_of_month', alias='month_of'),
    sr.SelectParameterOption('3', 'Weather Over Weeks', dim_col='start_of_week', alias='week_of')
]

# Filter By options
filter_by_options = sr.SelectionDataSource('time_type', 'index', 'value', custom_cols={'column': 'column'})

# Time Period options
time_period_options = sr.SelectionDataSource('time_lookup', 'index', 'start_of_time', parent_id_col='time_type_id')

# Parameters
group_by_param = sr.SingleSelectParameter('group_by', 'Group By', group_by_options)
trend_type_parameter = sr.SingleSelectParameter('trend_type', 'Trend Type', trend_type_options)
filter_by_parameter = sr.DataSourceParameter(sr.SingleSelectParameter, 'filter_by', 'Filter Time Period By', filter_by_options)
time_period_parameter = sr.DataSourceParameter(sr.MultiSelectParameter, 'time_period', 'Time Period of', time_period_options, 
                                               parent=filter_by_parameter)
