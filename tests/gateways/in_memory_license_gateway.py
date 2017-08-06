from typing import Optional

from cleancoderscom.entities.codecast import Codecast
from cleancoderscom.entities.license import License
from cleancoderscom.entities.user import User
from cleancoderscom.gateways.license_gateway import LicenseGateway
from tests.gateways.in_memory_gateway import InMemoryGateway


class InMemoryLicenseGateway(InMemoryGateway, LicenseGateway):
	def find_license_for(self, user: User, codecast: Codecast) -> Optional[License]:
		return next(filter(
			lambda x: x.user == user and x.codecast == codecast,
			self.find_all()), None)

