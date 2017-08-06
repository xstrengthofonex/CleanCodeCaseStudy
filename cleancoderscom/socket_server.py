import socket

from cleancoderscom.socket_service import SocketService


class SocketServer(object):
	def __init__(self, port: int, service: SocketService) -> None:
		self.port = port
		self.service = service
		self.running = False
		self.sock = None

	def start(self, timeout=None) -> None:
		self.running = True
		self.create_socket(timeout)
		while self.running:
			try:
				conn, addr = self.sock.accept()
				self.service.serve(conn)
				conn.close()
				continue
			except (socket.timeout, KeyboardInterrupt):
				break

	def create_socket(self, timeout):
		self.sock = socket.socket(socket.AF_INET, socket.SOL_SOCKET)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		try:
			self.sock.bind(("localhost", self.port))
			self.sock.listen(5)
			if timeout is not None:
				self.sock.settimeout(timeout)
		except OSError:
			self.sock.close()
			self.sock = None

	def stop(self) -> None:
		if self.sock is not None:
			self.sock.close()
			self.sock = None
		self.running = False

	def is_running(self) -> bool:
		return self.running
