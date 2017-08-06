from getgauge.python import step, continue_on_failure

from cleancoderscom.context import Context
from cleancoderscom.use_cases.present_codecasts_use_case import PresentCodecastsUseCase

boolean_mapper = {"+": True, "-": False}


@continue_on_failure
@step("ordered query of codecasts <table>")
def query_codecasts(table):
	logged_in_user = Context.gatekeeper.get_logged_in_user()
	presentable_codecasts = PresentCodecastsUseCase().present_codecasts(
		logged_in_user)
	for pcc, row in zip(presentable_codecasts, table):
		assert pcc.title == row[0]
		assert pcc.publication_date == row[1]
		assert pcc.is_viewable == boolean_mapper.get(row[4])
		assert pcc.is_downloadable == boolean_mapper.get(row[5])
