import unittest

from cleancoderscom.codecast import Codecast
from cleancoderscom.context import Context
from cleancoderscom.gatekeeper import GateKeeper
from cleancoderscom.license import License
from cleancoderscom.mock_gateway import MockGateway
from cleancoderscom.present_codecasts_use_case import PresentCodecastsUseCase
from cleancoderscom.user import User


class PresentCodecastsUseCaseTest(unittest.TestCase):
	def setUp(self):
		Context.gateway = MockGateway()
		Context.gatekeeper = GateKeeper()
		self.user = User("User")
		self.codecast = Codecast("A", "8/9/2017")
		Context.gateway.save_user(self.user)
		Context.gateway.save_codecast(self.codecast)
		self.use_case = PresentCodecastsUseCase()

	def test_user_without_view_license_cannot_view_codecast(self):
		self.assertFalse(self.use_case.is_licensed_to_view_codecast(
			self.user, self.codecast))

	def test_user_with_view_license_can_view_codecast(self):
		view_license = License(self.user, self.codecast)
		Context.gateway.save_license(view_license)
		self.assertTrue(self.use_case.is_licensed_to_view_codecast(
			self.user, self.codecast))

	def test_user_with_license_cannot_view_other_users_codecast(self):
		other_user = User("OtherUser")
		view_license = License(other_user, self.codecast)
		Context.gateway.save_license(view_license)
		self.assertFalse(self.use_case.is_licensed_to_view_codecast(
			self.user, self.codecast))