from typing import Optional

from CleanCodeCaseStudy.user import User


class GateKeeper(object):
	def __init__(self) -> None:
		self.logged_in_user = None   # type: Optional[User]

	def set_logged_in_user(self, user: User):
		self.logged_in_user = user

	def get_logged_in_user(self) -> Optional[User]:
		return self.logged_in_user
