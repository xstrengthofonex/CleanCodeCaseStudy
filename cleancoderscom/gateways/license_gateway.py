from abc import ABCMeta, abstractmethod
from typing import Optional

from cleancoderscom.entities.codecast import Codecast
from cleancoderscom.entities.license import License
from cleancoderscom.entities.user import User


class LicenseGateway(metaclass=ABCMeta):
	@abstractmethod
	def find_license_for(self, user: User, codecast: Codecast) -> Optional[License]:
		pass
