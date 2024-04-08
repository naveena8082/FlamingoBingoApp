import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Players')


def lambda_handler(event, context):
    print(event, "event")
    try:
        # Parse the player's email from the query string
        email_id = event['queryStringParameters']['email']

        # Retrieve the player's card
        response = table.get_item(Key={'email_id': email_id})
        item = response.get('Item', {})

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
            },
            'body': json.dumps(
                {'card': item.get('card', []), 'completions': item.get('completions', []), 'email_id': email_id,
                 'name': item.get('name', '')}),

        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {

                "Access-Control-Allow-Origin": "*",

            },
            'body': json.dumps({'error': str(e)})
        }