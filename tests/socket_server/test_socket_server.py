import unittest
import socket
from threading import Thread

import time

from cleancoderscom.socket_server import SocketServer
from tests.socket_server.fake_socket_service import FakeSocketService


class SocketServerTest(unittest.TestCase):
	def setUp(self):
		self.port = 3000
		self.host = "localhost"
		self.service = FakeSocketService()
		self.server = SocketServer(self.port, self.service)

	def test_instantiate(self):
		self.assertEqual(self.port, self.server.port)
		self.assertEqual(self.service, self.server.service)

	def test_can_start_and_stop_server(self):
		self.server.start(timeout=0.1)
		self.assertTrue(self.server.is_running())
		self.server.stop()
		self.assertFalse(self.server.is_running())

	def test_accepts_an_incoming_connection(self):
		thread = self.start_test_server_thread()
		self.start_test_connection()
		thread.join()
		self.server.stop()
		self.assertEqual(self.service.connections, 1)

	def test_accepts_multiple_incoming_connections(self):
		thread = self.start_test_server_thread()
		self.start_test_connection()
		self.start_test_connection()
		thread.join()
		self.server.stop()
		self.assertEqual(self.service.connections, 2)

	def start_test_connection(self, data=None):
		conn = socket.socket()
		conn.connect((self.host, self.port))
		if data:
			conn.sendall(data)
		conn.close()

	def start_test_server_thread(self):
		server_thread = Thread(target=self.server.start, kwargs={'timeout': 0.1})
		server_thread.start()
		time.sleep(0.01)
		return server_thread
