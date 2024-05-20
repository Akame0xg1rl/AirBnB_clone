#!/usr/bin/python3
"""
Contains the test cases for BaseModel class.
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.model = BaseModel()

    def test_instance_creation(self):
        """
        Test the creation of an instance of BaseModel.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_id(self):
        """
        Test that each instance has a unique ID.
        """
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_save_method(self):
        """
        Test the save method updates `updated_at`.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()

