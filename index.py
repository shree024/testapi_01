from awscli.errorhandler import ClientError

import test02
import logging

connection = test02.dynamoDB

#
# key_schema = [
#     {
#         "AttributeName": "username",
#         "KeyType": "HASH"
#     },
#     {
#         'AttributeName': 'email',
#         'KeyType': 'RANGE'
#     }
# ]
# attribute_definitions = [
#     {
#         "AttributeName": "username",
#         "AttributeType": "S"
#     },
#     {
#         'AttributeName': 'email',
#         'AttributeType': 'S'
#     }
# ]
# provisioned_throughput = {
#     "ReadCapacityUnits": 1,
#     "WriteCapacityUnits": 1
# }
#
#
# table_name = "userData"
#
# def create_table(table_name, key_schema, attribute_definitions, provisioned_throughput):
#     try:
#         dynamodb_resource = connection.create_table(TableName=table_name, KeySchema=key_schema,
#                                                     AttributeDefinitions=attribute_definitions,
#                                                     ProvisionedThroughput=provisioned_throughput)
#
#         # Wait until the table exists.
#         dynamodb_resource.meta.client.get_waiter('table_exists').wait(TableName=table_name)
#
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True
#



items={
    "name":"my dublin life",
    "username":"Pacasian",
    "place":"dublin",
    "token":"sightseeing",
    "details":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Odio facilisis mauris sit amet massa vitae tortor condimentum. Viverra adipiscing at in tellus integer. Duis ut diam quam nulla porttitor. Gravida rutrum quisque non tellus. Tellus molestie nunc non blandit massa enim. Proin sagittis nisl rhoncus mattis rhoncus urna. Sagittis nisl rhoncus mattis rhoncus. Sed euismod nisi porta lorem. Lacus luctus accumsan tortor posuere ac. Quis commodo odio aenean sed adipiscing diam donec. Sagittis id consectetur purus ut faucibus pulvinar elementum. Lectus nulla at volutpat diam ut venenatis tellus in. Quam vulputate dignissim suspendisse in est ante. Bibendum at varius vel pharetra vel turpis. Pellentesque id nibh tortor id. Lacinia quis vel eros donec ac. Dolor sed viverra ipsum nunc aliquet bibendum enim facilisis gravida. Nec nam aliquam sem et tortor consequat id porta. Felis eget velit aliquet sagittis id consectetur. Tortor at auctor urna nunc id cursus metus aliquam. Habitant morbi tristique senectus et netus et malesuada fames. Semper quis lectus nulla at volutpat diam. Nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. At varius vel pharetra vel turpis nunc eget lorem. Neque sodales ut etiam sit amet nisl. Cum sociis natoque penatibus et magnis dis parturient montes. Lorem sed risus ultricies tristique nulla aliquet enim. Lorem ipsum dolor sit amet consectetur adipiscing elit. Massa enim nec dui nunc mattis enim ut. Dignissim convallis aenean et tortor at risus. Nunc lobortis mattis aliquam faucibus purus in massa. Cursus mattis molestie a iaculis at erat pellentesque adipiscing commodo. Magnis dis parturient montes nascetur. Proin libero nunc consequat interdum varius. Fames ac turpis egestas integer eget aliquet nibh praesent. Sed euismod nisi porta lorem mollis. Nunc eget lorem dolor sed viverra ipsum nunc. Erat pellentesque adipiscing commodo elit at. Rhoncus mattis rhoncus urna neque viverra justo. Neque volutpat ac tincidunt vitae semper quis. Pretium nibh ipsum consequat nisl vel pretium lectus. Dolor sit amet consectetur adipiscing elit. Habitasse platea dictumst vestibulum rhoncus est. Condimentum mattis pellentesque id nibh tortor",
    "image":"None",
    "date":"12/07/1997"
}



# print(create_table(table_name, key_schema, attribute_definitions,provisioned_throughput))
def store_an_item( table_name, item):
    try:
        dynamodb_resource = connection
        table = dynamodb_resource.Table(table_name)
        table.put_item(Item=item)
    except ClientError as e:
        logging.error(e)
        return False
    return True


print(store_an_item("blogTable",items))