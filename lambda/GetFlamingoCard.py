import boto3
import json

# Initialize DynamoDB resource and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Players')

def get_player_info(email_id):
    try:
        # Retrieve the player's information from DynamoDB
        response = table.get_item(Key={'email_id': email_id})
        item = response.get('Item', {})
        return {
            'statusCode': 200,
            'body': json.dumps({
                'card': item.get('card', []),
                'completions': item.get('completions', []),
                'email_id': email_id,
                'name': item.get('name', '')
            }),
            'headers': {
                "Access-Control-Allow-Origin": "*",
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                "Access-Control-Allow-Origin": "*",
            }
        }

def lambda_handler(event, context):
    try:
        # Parse the player's email from the query string
        email_id = event['queryStringParameters']['email']
        return get_player_info(email_id)
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Email parameter is missing'}),
            'headers': {
                "Access-Control-Allow-Origin": "*",
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                "Access-Control-Allow-Origin": "*",
            }
        }
