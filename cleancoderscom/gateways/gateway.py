from abc import ABCMeta, abstractmethod
from typing import Optional, List

from cleancoderscom.entities.entity import Entity


class Gateway(metaclass=ABCMeta):
	@abstractmethod
	def find_all(self) -> List[Entity]:
		pass

	@abstractmethod
	def delete(self, entity: Entity) -> None:
		pass

	@abstractmethod
	def save(self, entity: Entity) -> Optional[Entity]:
		pass

	@abstractmethod
	def find(self, id_: str) -> Optional[Entity]:
		pass

