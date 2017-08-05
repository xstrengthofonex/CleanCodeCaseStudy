from typing import List

from cleancoderscom.codecast import Codecast
from cleancoderscom.context import Context
from cleancoderscom.presentable_codecast import PresentablCodecast
from cleancoderscom.user import User


class PresentCodecastsUseCase(object):
	@staticmethod
	def present_codecasts(logged_in_user: User) -> List[PresentablCodecast]:
		return []

	@staticmethod
	def is_licensed_to_view_codecast(user: User, codecast: Codecast) -> bool:
		return Context.gateway.find_license_for(user, codecast) is not None



