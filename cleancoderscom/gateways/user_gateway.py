from abc import ABCMeta, abstractmethod
from typing import Optional

from cleancoderscom.entities.user import User


class UserGateway(metaclass=ABCMeta):
	@abstractmethod
	def find_user(self, username: str) -> Optional[User]:
		pass
