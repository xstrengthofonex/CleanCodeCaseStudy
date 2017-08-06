from typing import Optional

from cleancoderscom.gatekeeper import GateKeeper
from cleancoderscom.gateways.codecast_gateway import CodecastGateway
from cleancoderscom.gateways.license_gateway import LicenseGateway
from cleancoderscom.gateways.user_gateway import UserGateway


class Context(object):
	license_gateway: Optional[LicenseGateway] = None
	codecast_gateway: Optional[CodecastGateway] = None
	user_gateway: Optional[UserGateway] = None
	gatekeeper: Optional[GateKeeper] = None
