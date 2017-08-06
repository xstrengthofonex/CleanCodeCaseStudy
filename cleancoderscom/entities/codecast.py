from datetime import datetime

from cleancoderscom.entities.entity import Entity


DateTime = datetime


class Codecast(Entity):
	def __init__(self, title: str, publication_date: DateTime) -> None:
		super().__init__()
		self.title = title
		self.publication_date = publication_date
