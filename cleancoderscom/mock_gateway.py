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

	def find_all_codecasts_ordered_by_date(self):
		return list(sorted(self.find_all_codecasts(),
						   key=lambda c: c.publication_date))

	def save_codecast(self, codecast: Type[Entity]) -> Type[Entity]:
		return self.save(codecast, self.codecasts)

	def save_user(self, user: Type[Entity]) -> Type[Entity]:
		return self.save(user, self.users)

	def save_license(self, view_license: Type[Entity]) -> Type[Entity]:
		return self.save(view_license, self.licenses)

	def save(self, entity: Type[Entity], entities) -> Type[Entity]:
		entity = self.establish_id(entity)
		entities.append(entity)
		return entity

	@staticmethod
	def establish_id(entity: Type[Entity]) -> Type[Entity]:
		if entity.id_ is None:
			entity.id_ = str(uuid.uuid4())
		return entity
