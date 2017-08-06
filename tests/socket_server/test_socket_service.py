from cleancoderscom.socket_service import SocketService


class TestSocketService(SocketService):
	connections = 0

	def __init__(self):
		self.message = ""

	def serve(self, conn):
		self.connections += 1
		data = conn.recv(1024)
		self.message += data.decode()
		conn.sendall(data)

