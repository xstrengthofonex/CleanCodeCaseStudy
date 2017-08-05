

class PresentableCodecast(object):
	def __init__(self, title: str, publication_date: str) -> None:
		self.title = title
		self.publication_date = publication_date
		self.is_viewable = False
		self.is_downloadable = False
