from CleanCodeCaseStudy.gateway import Gateway


class MockGateway(Gateway):
	def delete(self):
		pass

	def find_all_codecasts(self):
		return []
