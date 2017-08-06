from copy import copy

from getgauge.python import step, after_scenario, before_scenario, continue_on_failure

from cleancoderscom.context import Context
from cleancoderscom.entities.license import License
from cleancoderscom.entities.user import User
from cleancoderscom.present_codecasts_use_case import PresentCodecastsUseCase
from tests.test_context import TestContext


@before_scenario
def setup():
	TestContext.setup()


@after_scenario
def teardown():
	TestContext.teardown()


@continue_on_failure
@step("given no codecasts")
def clear_codecasts():
	codecasts = Context.codecast_gateway.find_all()
	for codecast in copy(codecasts):
		Context.codecast_gateway.delete(codecast)
	assert len(Context.codecast_gateway.find_all()) == 0


@continue_on_failure
@step("given user <username>")
def add_user(username):
	user = User(username)
	Context.user_gateway.save(user)
	assert True


@step("with user <username> logged in")
def login_user(username):
	user = Context.user_gateway.find_user(username)
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
	logged_in_user = Context.gatekeeper.get_logged_in_user()
	presentations = PresentCodecastsUseCase().present_codecasts(logged_in_user)
	assert len(presentations) == 0


@continue_on_failure
@step("and with license for <username> able to view <codecast>")
def create_license_for_viewing(username, codecast_title):
	user = Context.user_gateway.find_user(username)
	codecast = Context.codecast_gateway.find_codecast_by_title(codecast_title)
	view_license = License(user, codecast, License.VIEWING)
	Context.license_gateway.save(view_license)
	assert PresentCodecastsUseCase().is_licensed_for(License.VIEWING, user, codecast)


@continue_on_failure
@step("and with license for <username> able to download <codecast>")
def create_license_downloading(username, codecast_title):
	user = Context.user_gateway.find_user(username)
	codecast = Context.codecast_gateway.find_codecast_by_title(codecast_title)
	view_license = License(user, codecast, License.DOWNLOADING)
	Context.license_gateway.save(view_license)
	assert PresentCodecastsUseCase().is_licensed_for(License.DOWNLOADING, user, codecast)
