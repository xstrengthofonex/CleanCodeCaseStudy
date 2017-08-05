from CleanCodeCaseStudy.gateway import Gateway


class MockGateway(Gateway):
	def __init__(self):
		self.codecasts = []
		self.users = []

	def delete(self, codecast):
		self.codecasts.remove(codecast)

	def find_all_codecasts(self):
		return self.codecasts

	def find_user(self, username):
		return next(filter(lambda u: u.username == username, self.users), None)

	def save_codecast(self, codecast):
		self.save(codecast, self.codecasts)

	def save_user(self, user):
		self.save(user, self.users)

	@staticmethod
	def save(entity, entities):
		entities.append(entity)