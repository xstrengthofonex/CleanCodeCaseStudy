from cleancoderscom.socket_server import SocketServer
from cleancoderscom.socket_service import SocketService
from tests.gateways.in_memory_codecast_gateway import InMemoryCodecastGateway


class MainService(SocketService):
	def serve(self, conn):
		pass


class Main(object):
	def __init__(self):
		self.server = SocketServer(3000, MainService())
		self.codecast_gateway = InMemoryCodecastGateway()

	def get_server(self):
		return self.server

	def get_codecast_gateway(self):
		return self.codecast_gateway

