from datetime import datetime
from helpers.dates_helper import list_date_range, string_to_date


def test_string_to_date_default_format_true():
    format_date='%m/%d/%Y'
    string_date = '{d.month}/{d.day}/{d.year}'.format(
        d=datetime.strptime('9/27/2022', format_date)
        )
    
    datetiem_string_convertion = datetime.strptime(string_date,format_date)
    assert datetiem_string_convertion == string_to_date('9/27/2022',format_date), 'Expected date formats'
    assert type(datetiem_string_convertion) == type(string_to_date('9/27/2022',format_date)), 'Expected samte type'


def test_list_date_range_default_format_true():
    start_date=datetime

    list_date_range
    pass