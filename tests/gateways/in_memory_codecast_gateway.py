from typing import List, Optional

from cleancoderscom.entities.codecast import Codecast
from cleancoderscom.gateways.codecast_gateway import CodecastGateway
from tests.gateways.in_memory_gateway import InMemoryGateway


class InMemoryCodecastGateway(InMemoryGateway, CodecastGateway):
	def find_codecast_by_title(self, title: str) -> Optional[Codecast]:
		return next(filter(lambda c: c.title == title, self.find_all()), None)

	def find_all_codecasts_ordered_by_date(self) -> List[Codecast]:
		return list(sorted(self.find_all(),
						   key=lambda c: c.publication_date))

