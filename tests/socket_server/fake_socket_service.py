from cleancoderscom.socket_service import SocketService


class FakeSocketService(SocketService):
	connections = 0

	def __init__(self):
		self.message = ""

	def serve(self, conn):
		self.connections += 1
		self.message += conn.recv(1024).decode()

