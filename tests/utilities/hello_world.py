from cleancoderscom.socket_server import SocketServer
from cleancoderscom.socket_service import SocketService


class HelloWorld(SocketService):
	def serve(self, conn):
		body = "<h1>Hello, World!</h1>"
		response = "HTTP/1.1 200 OK\r\n"
		response += "Content-Type: text/html\r\n"
		response += "Content-Length: {}\r\n".format(len(body))
		response += "\r\n"
		response += body
		conn.sendall(response.encode())

	@staticmethod
	def main():
		port = 3000
		socket = SocketServer(port, HelloWorld())
		print("Serving on port {}".format(port))
		socket.start()

if __name__ == "__main__":
	HelloWorld.main()
