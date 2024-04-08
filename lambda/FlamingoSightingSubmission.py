import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Players')


def lambda_handler(event, context):
    try:
        # Parse the reported sighting
        body = json.loads(event['body'])
        region = body['region']

        # Scan the table to update all players' cards
        response = table.scan()
        print(response, "response")
        for item in response['Items']:
            print(item, "item")
            email_id = item['email_id']
            card = item['card']
            if region in card:
                index = card.index(region)
                table.update_item(
                    Key={'email_id': email_id},
                    UpdateExpression=f"SET completions[{index}] = :true",
                    ExpressionAttributeValues={':true': True}
                )

        return {
            'statusCode': 200,
            'headers': {

                "Access-Control-Allow-Origin": "*",

            },
            'body': json.dumps({'message': 'Sighting submitted successfully'})
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'headers': {

                "Access-Control-Allow-Origin": "*",

            },
            'body': json.dumps({'error': str(e)})
        }