import boto3
import json
import random
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Players')


def generate_bingo_card():
    regions = ["South America", "Gulf of Mexico", "West Africa", "South Africa", "Mediterranean", "East Asia",
               "Arabian Sea"]
    # Randomly pick 7 regions and add 2 free spaces
    card = random.sample(regions, 7) + [None, None]
    # Shuffle the card
    random.shuffle(card)
    return card
def lambda_handler(event, context):
    data = json.loads(event['body'])
    # Check if the username already exists
    response = table.get_item(
        Key={'email_id': data["email_id"]}
    )
    if 'Item' in response:
        return {
            'statusCode': 409,
            'headers': {
                "Access-Control-Allow-Origin": "*",
            },
            'body': 'Username already exists'
        }

    # If the username does not exist, create a new user
    try:
        email = data['email_id']
        name = data['name']

        # Generate a new Bingo card
        bingo_card = generate_bingo_card()

        # Store in DynamoDB
        response = table.put_item(
            Item={
                'email_id': email,
                'name': name,
                'card': bingo_card,
                'created_at': int(time.time()),
                'updated_at': int(time.time()),
                'completions': [False] * 9  # Initialize completions as False
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
            },
            'body': json.dumps(
                {'message': 'Player registered successfully', 'card': bingo_card, 'completions': [False] * 9})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                "Access-Control-Allow-Origin": "*",
            },
            'body': str(e)
        }