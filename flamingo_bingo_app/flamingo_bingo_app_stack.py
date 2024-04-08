from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk import aws_iam as iam
import os

class FlamingoBingoAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        cwd = os.getcwd()

        #Player Registration Service
        player_registration_lambda = _lambda.Function(
            self, "PlayerRegistrationHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="PlayerRegistration.lambda_handler",
            code=_lambda.Code.from_asset(os.path.join(cwd, "lambda")),
            description="Player Registration",
        )

        # Attach IAM policy to Lambda execution role
        player_registration_lambda.add_to_role_policy(
            statement=iam.PolicyStatement(
                actions=["dynamodb:*"],
                resources=["*"]
            )
        )

        # Flamingo_Sighting_Submission_Service

        flamingo_sighting_create_lambda = _lambda.Function(
            self, "FlamingoSightingSubmission",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="FlamingoSightingSubmission.lambda_handler",
            code=_lambda.Code.from_asset(os.path.join(cwd, "lambda")),
            description="Flamingo Sighting Submission",
        )

        flamingo_sighting_create_lambda.add_to_role_policy(
            statement=iam.PolicyStatement(
                actions=["dynamodb:*"],
                resources=["*"]
            )
        )


        #Get FlamingoCards Service

        get_flamingo_card_lambda = _lambda.Function(
            self, "GetFlamingoCardHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="GetFlamingoCard.lambda_handler",
            code=_lambda.Code.from_asset(os.path.join(cwd, "lambda")),
            description="Get Flamingo Card",
        )

        # Attach IAM policy to Lambda execution role
        get_flamingo_card_lambda.add_to_role_policy(
            statement=iam.PolicyStatement(
                actions=["dynamodb:*"],
                resources=["*"]
            )
        )






