from getgauge.python import step, continue_on_failure


@continue_on_failure
@step("given codecasts <table>")
def given_codecasts(table):
	assert False

