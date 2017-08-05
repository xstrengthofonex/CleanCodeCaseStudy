import uuid

from typing import List, Optional, Type

from cleancoderscom.codecast import Codecast
from cleancoderscom.entity import Entity
from cleancoderscom.gateway import Gateway
from cleancoderscom.license import License
from cleancoderscom.user import User


class MockGateway(Gateway):
	def __init__(self):
		self.codecasts: List[Codecast] = []
		self.users: List[User] = []
		self.licenses: List[License] = []

	def delete(self, codecast: Codecast) -> None:
		self.codecasts.remove(codecast)

	def find_all_codecasts(self) -> List[Codecast]:
		return self.codecasts

	def find_user(self, username: str) -> Optional[User]:
		return next(filter(lambda u: u.username == username, self.users), None)

	def find_codecast_by_title(self, title: str) -> Optional[Codecast]:
		return next(filter(lambda c: c.title == title, self.codecasts), None)

	def find_license_for(self, user: Type[Entity], codecast: Codecast) -> License:
		return next(filter(
			lambda x: x.user == user and x.codecast == codecast,
			self.licenses), None)

	def save_codecast(self, codecast: Type[Entity]) -> None:
		self.save(codecast, self.codecasts)

	def save_user(self, user: Type[Entity]) -> None:
		self.save(user, self.users)

	def save_license(self, viewing_license: Type[Entity]) -> None:
		self.save(viewing_license, self.licenses)

	def save(self, entity: Type[Entity], entities) -> None:
		entity = self.establish_id(entity)
		entities.append(entity)

	@staticmethod
	def establish_id(entity: Type[Entity]) -> Type[Entity]:
		if entity.id_ is None:
			entity.id_ = str(uuid.uuid4())
		return entity
