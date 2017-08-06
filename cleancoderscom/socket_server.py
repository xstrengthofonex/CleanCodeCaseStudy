import socket
from threading import Thread
from typing import Optional

from cleancoderscom.socket_service import SocketService

Socket = socket.socket


class SocketServer(object):
	def __init__(self, port: int, service: SocketService) -> None:
		self.port = port
		self.service = service
		self.running = False
		self.sock = None
		self.connections = []

	def start(self, timeout: Optional[float]=None) -> None:
		self.running = True
		self.sock = self.create_socket(timeout)
		while self.running:
			try:
				conn, addr = self.sock.accept()
				service_thread = Thread(target=self.service.serve, args=(conn,))
				service_thread.start()
				service_thread.join()
				conn.close()
				continue
			except (socket.timeout, KeyboardInterrupt):
				break
		self.sock.close()
		self.sock = None

	def create_socket(self, timeout: Optional[float]=None, queue: int=5) -> Socket:
		sock = socket.socket(socket.AF_INET, socket.SOL_SOCKET)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		try:
			sock.bind(("localhost", self.port))
			sock.listen(queue)
			if timeout is not None:
				sock.settimeout(timeout)
		except OSError:
			sock.close()
			sock = None
		return sock

	def stop(self) -> None:
		self.running = False

	def is_running(self) -> bool:
		return self.running
