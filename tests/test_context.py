from cleancoderscom.context import Context
from cleancoderscom.gatekeeper import GateKeeper
from cleancoderscom.mock_gateway import MockGateway


class TestContext(Context):
	@staticmethod
	def setup():
		Context.gateway = MockGateway()
		Context.gatekeeper = GateKeeper()

	@staticmethod
	def teardown():
		Context.gateway = None
		Context.gatekeeper = None
