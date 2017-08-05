from typing import List

from cleancoderscom.codecast import Codecast
from cleancoderscom.context import Context
from cleancoderscom.presentable_codecast import PresentableCodecast
from cleancoderscom.user import User
from tests.utilities import string_from_datetime


class PresentCodecastsUseCase(object):
	def present_codecasts(self, logged_in_user: User) -> List[PresentableCodecast]:
		presentable_codecasts = []
		codecasts = Context.gateway.find_all_codecasts_ordered_by_date()
		for codecast in codecasts:
			pcc = PresentableCodecast(
				title=codecast.title,
				publication_date=string_from_datetime(codecast.publication_date))
			pcc.is_viewable = self.is_licensed_to_view_codecast(
				logged_in_user, codecast)
			presentable_codecasts.append(pcc)
		return presentable_codecasts

	@staticmethod
	def is_licensed_to_view_codecast(user: User, codecast: Codecast) -> bool:
		return Context.gateway.find_license_for(user, codecast) is not None



