from getgauge.python import step, continue_on_failure


@continue_on_failure
@step("ordered query of codecasts <table>")
def query_codecasts(table):
	assert False
