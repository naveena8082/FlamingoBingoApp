from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda
    # aws_sqs as sqs,
)
from constructs import Construct

from . import flamingo_service


class FlamingoBingoAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        flamingo_service.FlamingoBingoService(self, "FlamingoBingo")








