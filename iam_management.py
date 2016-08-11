import boto3

client = boto3.client('iam')

# create a new user
response = client.create_user(UserName='sally')

# attach and delete user policy
response2 = client.attach_user_policy(UserName='sally', PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
response3 = client.detach_user_policy(UserName='sally', PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
