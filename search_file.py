import decimal
import json

from awscli.errorhandler import ClientError
from boto3.dynamodb.conditions import Key, Attr
import json

from flask import logging

import table_connection1

connection = table_connection1.table1
connection2 = table_connection1.table2


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def query_movies1(attr):
    try:
        response = connection.query(KeyConditionExpression=Key('username').eq(attr))
        res = response['Items']
        return res
    except ClientError as e:
        # print(e)
        return False
    return True





def login(usr, pwd):
    try:
        response = connection.get_item(
            Key={
                "username": usr,
                "password": pwd

            }
        )
        return json.loads(json.dumps(response['Item'], indent=4, cls=DecimalEncoder))
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}


def signUp( usr,pwd,name,status,phn,dob,email):
    try:
        table = connection
        table.put_item(Item={
            "username":usr,
            "password":pwd,
            "name":name,
            "status":status,
            "phone":phn,
            "dob":dob,
            "email":email,
            "interest":[],})
    except ClientError as e:
        logging.error(e)
        return False
    return True

def addBlog(name,usr,place,token,details,image,date):
    try:
        table = connection2
        table.put_item(Item={
                "name":name,
    "username":usr,
    "place":place,
    "token":token,
    "details":details,
    "image":image,
    "date":date})
    except ClientError as e:
        logging.error(e)
        return False
    return True

