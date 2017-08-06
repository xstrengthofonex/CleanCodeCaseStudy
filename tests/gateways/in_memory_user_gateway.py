from cleancoderscom.entities.user import User
from cleancoderscom.gateways.user_gateway import UserGateway
from tests.gateways.in_memory_gateway import InMemoryGateway


class InMemoryUserGateway(InMemoryGateway, UserGateway):
	def find_user(self, username: str) -> User:
		return next(filter(lambda u: u.username == username, self.find_all()), None)