from getgauge.python import step, continue_on_failure


from cleancoderscom.codecast import Codecast
from cleancoderscom.context import Context
from tests.utilities import datetime_from_string


@continue_on_failure
@step("given codecasts <table>")
def given_codecasts(table):
	for row in table:
		codecast = Codecast(title=row[0],
							publication_date=datetime_from_string(row[1]))
		Context.gateway.save_codecast(codecast)

