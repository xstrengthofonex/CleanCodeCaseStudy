from abc import ABCMeta, abstractmethod
from typing import List, Optional

from cleancoderscom.entities.codecast import Codecast


class CodecastGateway(metaclass=ABCMeta):
	@abstractmethod
	def find_all_codecasts_ordered_by_date(self) -> List[Codecast]:
		pass

	@abstractmethod
	def find_codecast_by_title(self, title) -> Optional[Codecast]:
		pass

