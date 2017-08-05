

class Entity(object):
	def __init__(self, id_: str = None) -> None:
		self.id_ = id_

	def __eq__(self, other) -> bool:
		if self.id_ and other.id_:
			return self.id_ == other.id_
		return False

