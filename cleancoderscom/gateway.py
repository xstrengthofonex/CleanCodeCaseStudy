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

	@abstractmethod
	def find_codecast_by_title(self, title):
		pass

	@abstractmethod
	def save_license(self, view_license):
		pass

	@abstractmethod
	def find_license_for(self, user, codecast):
		pass
