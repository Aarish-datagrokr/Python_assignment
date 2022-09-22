from operator import ge
from unittest import mock
from src.general_example import GeneralExample
import unittest

general_example_instance = GeneralExample()


class test_general_example(unittest.TestCase):

    def test_flatten_dictionary(self):
        test_parameter = {'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]}
        self.assertEqual(GeneralExample.flatten_dictionary(test_parameter), [0, 1, 2, 3, 10, 22, 42, 55])

    def test_load_employee_rec_from_database(self):
        test_parameter = ['emp001', 'Sam', '100000']
        self.assertEqual(GeneralExample.load_employee_rec_from_database(test_parameter), ['emp001', 'Sam', '100000'])

    @mock.patch('src.general_example.GeneralExample.fetch_emp_details', return_value=['emp001', 'Sam', '100000'])
    def test_fetch_emp_details(self, mock_check_output):
        expected = mock_check_output.return_value
        self.assertEqual(GeneralExample.fetch_emp_details(), expected)
