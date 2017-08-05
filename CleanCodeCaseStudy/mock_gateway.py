from CleanCodeCaseStudy.gateway import Gateway


class MockGateway(Gateway):
	def __init__(self):
		self.codecasts = []

	def delete(self, codecast):
		self.codecasts.remove(codecast)

	def find_all_codecasts(self):
		return self.codecasts

	def save(self, codecast):
		self.codecasts.append(codecast)