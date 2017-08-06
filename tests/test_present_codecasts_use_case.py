import unittest
from datetime import date

from cleancoderscom.context import Context
from cleancoderscom.entities.codecast import Codecast
from cleancoderscom.entities.license import License
from cleancoderscom.entities.user import User
from cleancoderscom.present_codecasts_use_case import PresentCodecastsUseCase
from tests.test_context import TestContext


class PresentCodecastsUseCaseTest(unittest.TestCase):
	def setUp(self):
		TestContext.setup()
		self.user = self.create_testable_user("User")
		self.codecast = self.create_testable_codecast("A", date(2017, 8, 2))
		self.use_case = PresentCodecastsUseCase()

	def tearDown(self):
		TestContext.teardown()

	def test_user_without_view_license_cannot_view_codecast(self):
		self.assertFalse(self.use_case.is_licensed_for(
			License.VIEWING, self.user, self.codecast))

	def test_user_with_view_license_can_view_codecast(self):
		self.create_testable_view_license(self.user, self.codecast)
		self.assertTrue(self.use_case.is_licensed_for(
			License.VIEWING, self.user, self.codecast))

	def test_user_with_license_cannot_view_other_users_codecast(self):
		other_user = self.create_testable_user("OtherUser")
		self.create_testable_view_license(other_user, self.codecast)
		self.assertFalse(self.use_case.is_licensed_for(
			License.VIEWING, self.user, self.codecast))

	def test_present_no_codecasts(self):
		Context.codecast_gateway.delete(self.codecast)
		presentable_codecasts = self.use_case.present_codecasts(self.user)
		self.assertEqual(0, len(presentable_codecasts))

	def test_present_one_codecast(self):
		self.create_testable_view_license(self.user, self.codecast)
		presentable_codecasts = self.use_case.present_codecasts(self.user)
		self.assertEqual(1, len(presentable_codecasts))
		presentable_codecast = presentable_codecasts[0]
		self.assertEqual("A", presentable_codecast.title)
		self.assertEqual("8/2/2017", presentable_codecast.publication_date)

	def test_presented_codecast_is_not_viewable_without_license(self):
		presentable_codecasts = self.use_case.present_codecasts(self.user)
		self.assertFalse(presentable_codecasts[0].is_viewable)

	def test_presented_codecast_is_viewable_with_view_license(self):
		self.create_testable_view_license(self.user, self.codecast)
		presentable_codecasts = self.use_case.present_codecasts(self.user)
		self.assertTrue(presentable_codecasts[0].is_viewable)

	def test_presented_codecast_is_downloadable_with_download_license(self):
		self.create_testable_download_license(self.user, self.codecast)
		presentable_codecasts = self.use_case.present_codecasts(self.user)
		self.assertTrue(presentable_codecasts[0].is_downloadable)

	@staticmethod
	def create_testable_user(username):
		return Context.user_gateway.save(User(username))

	@staticmethod
	def create_testable_codecast(title, publication_date):
		return Context.codecast_gateway.save(
			Codecast(title, publication_date))

	@staticmethod
	def create_testable_view_license(user, codecast):
		return Context.license_gateway.save(
			License(user, codecast, License.VIEWING))

	@staticmethod
	def create_testable_download_license(user, codecast):
		return Context.license_gateway.save(
			License(user, codecast, License.DOWNLOADING))