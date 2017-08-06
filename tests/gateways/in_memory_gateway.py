import threading
import uuid
from copy import deepcopy

from typing import Type, Dict, Optional

from cleancoderscom.entities.entity import Entity
from cleancoderscom.gateways.gateway import Gateway


class InMemoryGateway(Gateway):
	def __init__(self):
		self.entities: Dict[str, Entity] = {}
		self.lock = threading.Lock()

	def delete(self, entity: Entity) -> None:
		with self.lock:
			self.entities.pop(entity.id_)

	def find_all(self):
		return deepcopy(list(self.entities.values()))

	def find(self, id_: str) -> Optional[Entity]:
		return next(filter(lambda e: e.id_ == id_, self.find_all()), None)

	def save(self, entity: Entity) -> Optional[Entity]:
		with self.lock:
			entity = self.establish_id(entity)
			self.entities[entity.id_] = deepcopy(entity)
			return entity

	@staticmethod
	def establish_id(entity: Entity) -> Entity:
		if entity.id_ is None:
			entity.id_ = str(uuid.uuid4())
		return entity
