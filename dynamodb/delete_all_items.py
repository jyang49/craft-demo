import util

table_name = 's3_object_list'

dynamodb = util.get_resource('dynamodb')
table = dynamodb.Table(table_name)

response = table.scan()
for i in response['Items']:
    Key = {
        'object_name': i['object_name']
    }
    print('Deleting ' + i['object_name'])
    table.delete_item(Key=Key)