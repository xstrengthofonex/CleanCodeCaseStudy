import unittest

from cleancoderscom.entity import Entity


class EntityTest(unittest.TestCase):
	def setUp(self):
		self.e1 = Entity("e1")
		self.e2 = Entity("e2")

	def test_two_different_entities_are_not_the_same(self):
		self.e1.id_ = "e1ID"
		self.e2.id_ = "e2ID"
		self.assertFalse(self.e1 == self.e2)

	def test_one_entity_is_same_as_itself(self):
		self.e1.id_ = "e1ID"
		self.assertTrue(self.e1 == self.e1)

	def test_entity_with_the_same_id_are_the_same(self):
		self.e1.id_ = "e1ID"
		self.e2.id_ = "e1ID"
		self.assertTrue(self.e1 == self.e2)

	def test_entity_with_none_id_are_not_the_same(self):
		self.e1.id_ = None
		self.e2.id_ = None
		self.assertFalse(self.e1 == self.e2)