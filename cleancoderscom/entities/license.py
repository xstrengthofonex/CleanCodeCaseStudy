from enum import Enum

from cleancoderscom.entities.codecast import Codecast
from cleancoderscom.entities.entity import Entity
from cleancoderscom.entities.user import User


class LicenseType(Enum):
	DOWNLOADING = "downloading"
	VIEWING = "viewing"


class License(Entity):
	DOWNLOADING = LicenseType.DOWNLOADING
	VIEWING = LicenseType.VIEWING

	def __init__(self, user: User, codecast: Codecast,
				 license_type: LicenseType) -> None:
		super().__init__()
		self.user = user
		self.codecast = codecast
		self.license_type = license_type
