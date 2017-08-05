from cleancoderscom.entity import Entity


class User(Entity):
	def __init__(self, username):
		super().__init__()
		self.username = username
