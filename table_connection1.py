import boto3


dynamoDB  = boto3.resource("dynamodb", aws_access_key_id="ASIASL3ROMC5P76W6T2W",
                       aws_secret_access_key="IyaiZ5Ldx4BiUnk9HRBuZq4Nnh30270m1YoqSnzd",
                       aws_session_token="FwoGZXIvYXdzEEsaDD9wlCNiTBqSgSoISyLKAQ/P0kEVMJMd1TrDzneDI786IpM+r/nozXQeTV8L/NRubNvFMOwVEul3AIFypD4rnNLpBJaz+z2xkMywMMgv9pDT101lXk/P9wDo5J25HJ/BDn5VbybrT/5fze4X50TwhHe93zTrPDOg8rB0M1KxMoNhq+CYwW/M7OIB3H+yZ4MBGoKd/ak4gmHsfth+jiM2kBqwFnhXoVAboZMnH22MUHunowbNBJBW+YA8Ip0jDyVNHHvHZSkVEIHqLGn0AFD55z+/8WOGY7r989Eo6M+sjAYyLYZ4i8pTw9i33cV1CcElyReodXHhutQBtkHsuBG4uuLaLO/4k3s6E4t1nsjdFA==")

table1= dynamoDB.Table('userTable')
table2= dynamoDB.Table('blogTable')
