import boto3
ENDPOINT = "http://localhost:8000"
REGION = "eu-central-1"

dynamodb = boto3.resource('dynamodb', region_name= REGION, endpoint_url=ENDPOINT)

dynamodb_client = boto3.client('dynamodb')

data = dict()
info = dict()
zaehne = dict()
def new_table(self):
    try:
        table = dynamodb.create_table(

            TableName='Patient',
            KeySchema=[
                {
                    'AttributeName': 'piz',
                    'KeyType': 'HASH'  #Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'piz',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        print("Table status:", table.table_status)
    except dynamodb_client.exceptions.ResourceInUseException:
        print("Exception")
            
def new_entry(self):
    table = dynamodb.Table('Patient')
    Item= data
    Item['info'] = info
    Item['zaehne'] = zaehne
    table.put_item(Item)
      
def set_value(dict, key, value):
    if dict == "data":
        data[key] = value
        print(data)
    if dict == "info":
        info[key] = value
        print(info)
    if dict == "zaehne":
        zaehne[key] = value
        print(zaehne)
        
def printAll():
    data["info"] =info
    data["zaehne"] =zaehne
    print(data)


