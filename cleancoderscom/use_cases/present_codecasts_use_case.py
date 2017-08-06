from typing import List

from cleancoderscom.context import Context
from cleancoderscom.entities.codecast import Codecast
from cleancoderscom.entities.license import License, LicenseType
from cleancoderscom.entities.user import User
from cleancoderscom.use_cases.presentable_codecast import PresentableCodecast
from cleancoderscom.utilities import string_from_datetime


class PresentCodecastsUseCase(object):
	def present_codecasts(self, logged_in_user: User) -> List[PresentableCodecast]:
		presentable_codecasts = []
		codecasts = Context.codecast_gateway.find_all_codecasts_ordered_by_date()
		for codecast in codecasts:
			presentable_codecasts.append(self.format_codecast(codecast, logged_in_user))
		return presentable_codecasts

	def format_codecast(self, codecast, logged_in_user):
		pcc = PresentableCodecast(codecast.title, string_from_datetime(codecast.publication_date))
		pcc.is_viewable = self.is_licensed_for(License.VIEWING, logged_in_user, codecast)
		pcc.is_downloadable = self.is_licensed_for(License.DOWNLOADING, logged_in_user, codecast)
		return pcc

	@staticmethod
	def is_licensed_for(license_type: LicenseType, user: User, codecast: Codecast) -> bool:
		license_ = Context.license_gateway.find_license_for(user, codecast)
		if license_ and license_.license_type == license_type:
			return True
		return False


