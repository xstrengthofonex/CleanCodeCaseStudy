from cleancoderscom.entity import Entity


class Codecast(Entity):
	def __init__(self, title: str, publication_date: str) -> None:
		super().__init__()
		self.title = title
		self.publication_date = publication_date
