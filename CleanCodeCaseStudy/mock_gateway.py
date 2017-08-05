from typing import List, Optional

from CleanCodeCaseStudy.codecast import Codecast
from CleanCodeCaseStudy.gateway import Gateway
from CleanCodeCaseStudy.user import User


class MockGateway(Gateway):
	def __init__(self):
		self.codecasts = []   # type: List[Codecast]
		self.users = []       # type: List[User]

	def delete(self, codecast: Codecast) -> None:
		self.codecasts.remove(codecast)

	def find_all_codecasts(self) -> List[Codecast]:
		return self.codecasts

	def find_user(self, username: str) -> Optional[User]:
		return next(filter(lambda u: u.username == username, self.users), None)

	def save_codecast(self, codecast: Codecast) -> None:
		self.save(codecast, self.codecasts)

	def save_user(self, user: User) -> None:
		self.save(user, self.users)

	@staticmethod
	def save(entity, entities) -> None:
		entities.append(entity)