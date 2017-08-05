from getgauge.python import step, after_scenario, before_scenario, continue_on_failure

from CleanCodeCaseStudy.context import Context
from CleanCodeCaseStudy.mock_gateway import MockGateway


@before_scenario
def setup():
	Context.gateway = MockGateway()


@after_scenario
def teardown():
	pass


@continue_on_failure
@step("given no codecasts")
def clear_codecasts():
	codecasts = Context.gateway.find_all_codecasts()
	for codecast in codecasts:
		Context.gateway.delete(codecast)
	assert len(Context.gateway.find_all_codecasts()) == 0


@continue_on_failure
@step("given user <username>")
def add_user(username):
	assert False


@step("with user <username> logged in")
def login_user(username):
	assert False


@continue_on_failure
@step("then the following codecasts will be presented for <username>")
def presentation_user(username):
	assert False


@continue_on_failure
@step("there will be no codecasts presented")
def count_of_codecasts():
	assert False


@continue_on_failure
@step("and with license for <username> able to view <codecast>")
def create_license_for_viewing(username, codecast_title):
	assert False
