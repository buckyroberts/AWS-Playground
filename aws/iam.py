import boto3
from settings import *

client = boto3.client('iam')

# create a new user
response = client.create_user(UserName=USERNAME)

# attach and delete user policy
response2 = client.attach_user_policy(UserName=USERNAME, PolicyArn=POLICY_ARN)
response3 = client.detach_user_policy(UserName=USERNAME, PolicyArn=POLICY_ARN)
