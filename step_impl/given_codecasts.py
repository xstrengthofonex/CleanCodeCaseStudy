from getgauge.python import step, continue_on_failure

from cleancoderscom.codecast import Codecast
from cleancoderscom.context import Context


@continue_on_failure
@step("given codecasts <table>")
def given_codecasts(table):
	for row in table:
		codecast = Codecast(row[0], row[1])
		Context.gateway.save_codecast(codecast)

