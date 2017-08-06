from abc import ABCMeta, abstractmethod


class SocketService(metaclass=ABCMeta):
	@abstractmethod
	def serve(self, conn):
		pass

