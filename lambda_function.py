import json
import boto3

dbclient = boto3.client('dynamodb')
dbtable = 'Visitor_Count'

def lambda_handler(event, context):
    response = dbclient.update_item(
        TableName = dbtable,
        Key = {
            'id' : {'S' : 'visitor-count'}
        },
        UpdateExpression = 'ADD visitor :inc',
        ExpressionAttributeValues = {':inc' : {'N' : '1'}},
        ReturnValues = 'UPDATED_NEW'
    )
    
    # final = int(response["Attributes"]["visitor"]["N"])
    final = json.dumps({"counter": int(response["Attributes"]["visitor"]["N"])})
    
    
    # apiResponse = {
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        'body': final
    }


    # Return api response object
    # return apiResponse