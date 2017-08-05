from datetime import datetime


def datetime_from_string(string, date_format="%m/%d/%Y"):
	return datetime.strptime(string, date_format)


def string_from_datetime(datetime_obj, date_format="%-m/%-d/%Y"):
	return datetime_obj.strftime(date_format)