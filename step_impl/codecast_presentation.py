from copy import copy

from getgauge.python import step, after_scenario, before_scenario, continue_on_failure

from CleanCodeCaseStudy.context import Context
from CleanCodeCaseStudy.gatekeeper import GateKeeper
from CleanCodeCaseStudy.mock_gateway import MockGateway
from CleanCodeCaseStudy.present_codecasts_use_case import PresentCodecastsUseCase
from CleanCodeCaseStudy.user import User


@before_scenario
def setup():
	Context.gateway = MockGateway()
	Context.gatekeeper = GateKeeper()


@after_scenario
def teardown():
	pass


@continue_on_failure
@step("given no codecasts")
def clear_codecasts():
	codecasts = Context.gateway.find_all_codecasts()
	for codecast in copy(codecasts):
		Context.gateway.delete(codecast)
	assert len(Context.gateway.find_all_codecasts()) == 0


@continue_on_failure
@step("given user <username>")
def add_user(username):
	user = User(username)
	Context.gateway.save_user(user)
	assert True


@step("with user <username> logged in")
def login_user(username):
	user = Context.gateway.find_user(username)
	if user:
		Context.gatekeeper.set_logged_in_user(user)
		assert True
	else:
		assert False


@continue_on_failure
@step("then the following codecasts will be presented for <username>")
def presentation_user(username):
	user = Context.gatekeeper.get_logged_in_user()
	assert user.username == username


@continue_on_failure
@step("there will be no codecasts presented")
def count_of_codecasts():
	codecasts = PresentCodecastsUseCase().present_codecasts()
	assert len(codecasts) == 0


@continue_on_failure
@step("and with license for <username> able to view <codecast>")
def create_license_for_viewing(username, codecast_title):
	assert False
