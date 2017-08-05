from typing import Optional, ClassVar

from cleancoderscom.gatekeeper import GateKeeper
from cleancoderscom.gateway import Gateway


class Context(object):
	gateway: ClassVar[Optional[Gateway]] = None
	gatekeeper: ClassVar[Optional[GateKeeper]] = None
