import os
from constructs import Construct
from aws_cdk import (
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb,
    aws_iam as iam,
    aws_lambda as _lambda,
    Stack,
)

class FlamingoBingoService(Construct):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Initialize DynamoDB table
        # table = self.create_dynamodb_table()

        # Lambda functions
        player_registration_lambda = self.create_dynamodb_table(
            handler="PlayerRegistration.lambda_handler", description="Player Registration V2"
        )
        flamingo_sighting_create_lambda = self.create_dynamodb_table(
            handler="FlamingoSightingSubmission.lambda_handler", description="Flamingo Sighting Submission V2"
        )
        get_flamingo_card_lambda = self.create_dynamodb_table(
            handler="GetFlamingoCard.lambda_handler", description="Get Flamingo Card V2"
        )

        # Attach IAM policy to Lambda execution roles
        self.attach_lambda_policy(player_registration_lambda)
        self.attach_lambda_policy(flamingo_sighting_create_lambda)
        self.attach_lambda_policy(get_flamingo_card_lambda)

        # API Gateway
        api = self.create_api_gateway()

        # Define resources and methods
        self.add_resource_method(api, "player-registration", "POST", player_registration_lambda)
        self.add_resource_method(api, "flamingo-sighting", "POST", flamingo_sighting_create_lambda)
        self.add_resource_method(api, "get-flamingo-card", "GET", get_flamingo_card_lambda)

    
    def create_dynamodb_table(self):
        return dynamodb.Table(
            self, "Player",
            partition_key=dynamodb.Attribute(name="email_id", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="created_at", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            time_to_live_attribute="updated_at",
            attributes={
                'name': dynamodb.Attribute(name="name", type=dynamodb.AttributeType.STRING),
                'card': dynamodb.Attribute(name="card", type=dynamodb.AttributeType.LIST),
                'completions': dynamodb.Attribute(name="completions", type=dynamodb.AttributeType.LIST),
                'created_at': dynamodb.Attribute(name="created_at", type=dynamodb.AttributeType.NUMBER),
                'updated_at': dynamodb.Attribute(name="updated_at", type=dynamodb.AttributeType.NUMBER),
            }
        )

    def create_dynamodb_table(self, handler, description):
        cwd = os.getcwd()
        return _lambda.Function(
            self, description.split()[0],
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler=handler,
            code=_lambda.Code.from_asset(os.path.join(cwd, "lambda")),
            description=description,
        )

    def attach_lambda_policy(self, lambda_function):
        lambda_function.add_to_role_policy(
            statement=iam.PolicyStatement(
                actions=["dynamodb:*"],
                resources=["*"]
            )
        )

    def create_api_gateway(self):
        return apigateway.RestApi(
            self, "flamingo-api",
            rest_api_name="Flamingo Services V1",
            description="This service serves for flamingo bingo gaming",
            default_cors_preflight_options={
                "allow_origins": apigateway.Cors.ALL_ORIGINS,
                "allow_methods": apigateway.Cors.ALL_METHODS
            })

    def add_resource_method(self, api, resource_path, method, lambda_integration):
        resource = api.root.add_resource(resource_path)
        resource.add_method(method, apigateway.LambdaIntegration(lambda_integration))
