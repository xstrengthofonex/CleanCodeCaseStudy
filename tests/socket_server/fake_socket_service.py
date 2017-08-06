from cleancoderscom.socket_service import SocketService


class FakeSocketService(SocketService):
	connections = 0

	def serve(self, conn):
		self.connections += 1

