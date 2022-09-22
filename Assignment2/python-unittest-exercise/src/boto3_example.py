import boto3


class S3Example(object):
    def __init__(self, bucket_name, name, value):
        self.bucket_name = bucket_name
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.put_object(Bucket=self.bucket_name, Key=self.name, Body=self.value)


class DynamodBExample(object):
    def __init__(self):
        print('Initializing class')

    def create_movies_table(self) -> None:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        table = dynamodb.create_table(
            TableName='Movies',
            KeySchema=[
                {
                    'AttributeName': 'year',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'title',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'year',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'title',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName='Movies')
        assert table.table_status == 'ACTIVE'

        return table

    def add_dynamo_record(self,title, year):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        table = dynamodb.Table('Movies')
        response = table.put_item(
             Item={
            'year': year,
            'title': title
        }
    )
        return response
