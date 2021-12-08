from awscli.errorhandler import ClientError

import test02
import logging

connection = test02.dynamoDB

key_schema = [
    {
        "AttributeName": "name",
        "KeyType": "HASH"
    },
    {
        'AttributeName': 'place',
        'KeyType': 'RANGE'
    }
]
attribute_definitions = [
    {
        "AttributeName": "name",
        "AttributeType": "S"
    },
    {
        'AttributeName': 'place',
        'AttributeType': 'S'
    }
]
provisioned_throughput = {
    "ReadCapacityUnits": 1,
    "WriteCapacityUnits": 1
}


table_name = "sampleTable"

def create_table(table_name, key_schema, attribute_definitions, provisioned_throughput):
    try:
        dynamodb_resource = connection.create_table(TableName=table_name, KeySchema=key_schema,
                                                    AttributeDefinitions=attribute_definitions,
                                                    ProvisionedThroughput=provisioned_throughput)

        # Wait until the table exists.
        dynamodb_resource.meta.client.get_waiter('table_exists').wait(TableName=table_name)

    except ClientError as e:
        logging.error(e)
        return False
    return True

create_table(table_name,key_schema,attribute_definitions,provisioned_throughput)