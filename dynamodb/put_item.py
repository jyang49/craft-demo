import boto3
import sys
import util

table_name = 's3_object_list'
object_name = sys.argv[1]

Item = {
    'object_name': object_name,
    'in_processing': 'n',
    'processing_completed': 'n'
}

dynamodb = util.get_resource('dynamodb')

table = dynamodb.Table(table_name)

table.put_item(
    Item=Item
)