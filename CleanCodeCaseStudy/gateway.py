from abc import ABCMeta, abstractmethod


class Gateway(metaclass=ABCMeta):
	@abstractmethod
	def find_all_codecasts(self):
		pass

	@abstractmethod
	def delete(self, entity):
		pass

	@abstractmethod
	def save_codecast(self, codecast):
		pass

	@abstractmethod
	def save_user(self, user):
		pass

	@abstractmethod
	def find_user(self, username):
		pass
