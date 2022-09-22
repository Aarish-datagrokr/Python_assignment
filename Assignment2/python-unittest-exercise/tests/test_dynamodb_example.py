import unittest

import boto3
from moto import mock_dynamodb2
from src.boto3_example import DynamodBExample


@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table = DynamodBExample.create_movies_table(self.dynamodb)

    def test_create_dynamo_table(self):
        self.assertIn('Movies', self.table.name)  # check if the table name is 'Movies'
    def test_add_dynamo_record_table(self):
        model_instance = DynamodBExample()
        result = model_instance.add_dynamo_record("The Big New Movie", 2015)
        self.assertEqual(200, result['ResponseMetadata']['HTTPStatusCode'])
