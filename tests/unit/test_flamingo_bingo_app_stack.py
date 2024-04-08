import aws_cdk as core
import aws_cdk.assertions as assertions

from flamingo_bingo_app.flamingo_bingo_app_stack import FlamingoBingoAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in flamingo_bingo_app/flamingo_bingo_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FlamingoBingoAppStack(app, "flamingo-bingo-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
