from cleancoderscom.codecast import Codecast
from cleancoderscom.entity import Entity
from cleancoderscom.user import User


class License(Entity):
	def __init__(self, user: User, codecast: Codecast) -> None:
		super().__init__()
		self.user = user
		self.codecast = codecast
