from abc import ABCMeta, abstractmethod


class Gateway(metaclass=ABCMeta):
	@abstractmethod
	def find_all_codecasts(self):
		pass

	@abstractmethod
	def delete(self, entity):
		pass

	@abstractmethod
	def save(self, entity):
		pass

