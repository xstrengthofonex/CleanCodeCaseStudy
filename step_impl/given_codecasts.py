from getgauge.python import step, continue_on_failure

from cleancoderscom.context import Context
from cleancoderscom.entities.codecast import Codecast
from tests.utilities import datetime_from_string


@continue_on_failure
@step("given codecasts <table>")
def given_codecasts(table):
	for row in table:
		codecast = Codecast(title=row[0],
							publication_date=datetime_from_string(row[1]))
		Context.codecast_gateway.save(codecast)

