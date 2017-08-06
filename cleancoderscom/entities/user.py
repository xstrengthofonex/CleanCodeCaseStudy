from cleancoderscom.entities.entity import Entity


class User(Entity):
	def __init__(self, username: str) -> None:
		super().__init__()
		self.username = username
