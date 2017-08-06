from cleancoderscom.context import Context
from cleancoderscom.gatekeeper import GateKeeper
from tests.gateways.in_memory_codecast_gateway import InMemoryCodecastGateway
from tests.gateways.in_memory_license_gateway import InMemoryLicenseGateway
from tests.gateways.in_memory_user_gateway import InMemoryUserGateway


class TestContext(Context):
	@staticmethod
	def setup() -> None:
		Context.user_gateway = InMemoryUserGateway()
		Context.license_gateway = InMemoryLicenseGateway()
		Context.codecast_gateway = InMemoryCodecastGateway()
		Context.gatekeeper = GateKeeper()

	@staticmethod
	def teardown() -> None:
		Context.gateway = None
		Context.gatekeeper = None
