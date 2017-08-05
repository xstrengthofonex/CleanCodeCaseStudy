from typing import List

from CleanCodeCaseStudy.presentable_codecast import PresentablCodecast
from CleanCodeCaseStudy.user import User


class PresentCodecastsUseCase(object):
	@staticmethod
	def present_codecasts(logged_in_user: User) -> List[PresentablCodecast]:
		return []
