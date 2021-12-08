
import boto3


dynamoDB  = boto3.resource("dynamodb", aws_access_key_id="ASIASL3ROMC5P76W6T2W",
                       aws_secret_access_key="IyaiZ5Ldx4BiUnk9HRBuZq4Nnh30270m1YoqSnzd",
                       aws_session_token="FwoGZXIvYXdzEEsaDD9wlCNiTBqSgSoISyLKAQ/P0kEVMJMd1TrDzneDI786IpM+r/nozXQeTV8L/NRubNvFMOwVEul3AIFypD4rnNLpBJaz+z2xkMywMMgv9pDT101lXk/P9wDo5J25HJ/BDn5VbybrT/5fze4X50TwhHe93zTrPDOg8rB0M1KxMoNhq+CYwW/M7OIB3H+yZ4MBGoKd/ak4gmHsfth+jiM2kBqwFnhXoVAboZMnH22MUHunowbNBJBW+YA8Ip0jDyVNHHvHZSkVEIHqLGn0AFD55z+/8WOGY7r989Eo6M+sjAYyLYZ4i8pTw9i33cV1CcElyReodXHhutQBtkHsuBG4uuLaLO/4k3s6E4t1nsjdFA==")

# def query_movies1( yea):
#     try:
#         # table = boto3.resource('dynamodb', aws_access_key_id="ASIAVPQN3PX2IXDBCMPI",
#         #             aws_secret_access_key="cuZXriJpw7QwKOR6+O4ivs1hKqqptldhbM3l2+4w",
#         #             aws_session_token="FwoGZXIvYXdzECwaDA6Nu1Gzfjl/p3Ci1SLKAbEM9gYQl4Zs0Gu1/psC0+8ShGl2zNfEYDJBG5AlASsIOqdw6hMbgjVUM5OrAn2WZscvD+/+KZKCo7dSyvDwfChWCLpcV6jEbgyciUaRqcHkqdgaDhYhbZib4BLJMxkaHUk/Ik+FNgPh7PaA4k/pUoKoti/pCrHvN6HAonUGfnTQ7HF+Bx0MuPUCGklWoyVOJSKFZLYtf6kMG2ZEkfiZhuiuUpcc6/4RIgnwep8U8TKW8gZDA3Zbip3N291qA12D0cjUEobh7EIqzEwoyNSljAYyLdsH+oOob8B6SqVlrSXTM28Jl7vK2Vp9lqmn8RNSbf+GM5Ryxcz1AG5FKNPNtw==").Table(table_name)
#         response = table.query(KeyConditionExpression=Key('year').eq(yea))
#         print(type(response['Items']))
#         res= response['Items']
#         # print(len(res))
#         print(res[0])
#
#         return "sumith"
#     except ClientError as e:
#         print(e)
#         return False
#     return True
#
#
#
# print(query_movies1(2013))
#
#
#
