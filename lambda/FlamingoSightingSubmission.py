import boto3
import json

# Initialize DynamoDB resource and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Players')


def update_player_completions(email_id, region):
    try:
        # Retrieve player's card
        response = table.get_item(Key={'email_id': email_id})
        if 'Item' not in response:
            return False, 'Player not found'

        player = response['Item']
        card = player.get('card', [])

        # Update completions for the given region
        if region in card:
            index = card.index(region)
            table.update_item(
                Key={'email_id': email_id},
                UpdateExpression=f"SET completions[{index}] = :true",
                ExpressionAttributeValues={':true': True}
            )
            return True, 'Completions updated successfully'
        else:
            return False, 'Region not found in player card'
    except Exception as e:
        return False, str(e)


def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event['body'])
        region = body['region']

        # Scan the table to update all players' cards
        response = table.scan()
        for item in response['Items']:
            email_id = item['email_id']
            success, message = update_player_completions(email_id, region)
            if not success:
                raise Exception(message)

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
            },
            'body': json.dumps({'message': 'Sighting submitted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                "Access-Control-Allow-Origin": "*",
            },
            'body': json.dumps({'error': str(e)})
        }
