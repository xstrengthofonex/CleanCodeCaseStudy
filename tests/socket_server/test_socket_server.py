import unittest
import socket
from threading import Thread
import time

from cleancoderscom.socket_server import SocketServer
from tests.socket_server.fake_socket_service import FakeSocketService


class TestServerContext(object):
	def __init__(self, server):
		self.server = server
		self.server_thread = None

	def __enter__(self):
		self.server_thread = Thread(target=self.server.start, kwargs={'timeout': 0.1})
		self.server_thread.start()
		time.sleep(0.01)

	def __exit__(self, *exc):
		self.server_thread.join()
		self.server_thread = None
		self.server.stop()


class TestConnectionContext(object):
	def __init__(self, host, port):
		self.conn = None
		self.host = host
		self.port = port

	def __enter__(self):
		self.conn = socket.socket()
		self.conn.connect((self.host, self.port))
		return self.conn

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.conn.close()


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
		with self.get_test_server_context():
			with self.get_test_connection_context():
				pass
		self.assertEqual(self.service.connections, 1)

	def test_accepts_multiple_incoming_connections(self):
		with self.get_test_server_context():
			with self.get_test_connection_context():
				pass
			with self.get_test_connection_context():
				pass
		self.assertEqual(self.service.connections, 2)

	def test_can_send_and_recv_data(self):
		with self.get_test_server_context():
			with self.get_test_connection_context() as conn:
				conn.sendall(b"Hello")
		self.assertEqual(self.service.message, "Hello")

	def test_can_send_and_recv_multiple_messages(self):
		with self.get_test_server_context():
			with self.get_test_connection_context() as conn:
				conn.sendall(b"Hello")
			with self.get_test_connection_context() as conn:
				conn.sendall(b"Test")
		self.assertEqual(self.service.message, "HelloTest")

	def get_test_server_context(self):
		return TestServerContext(self.server)

	def get_test_connection_context(self):
		return TestConnectionContext(self.host, self.port)



