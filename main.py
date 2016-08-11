import boto3
from settings import *

ec2 = boto3.resource('ec2')

# maybe create two instances and then just change the tags (name) individually
ec2.create_instances(ImageId=IMAGE_ID, MinCount=1, MaxCount=1, InstanceType=INSTANCE_TYPE)

# check what instances are running
for instance in ec2.instances.all():
    print(instance.id, instance.tags)

# adds or overwrites one or more tags
response = ec2.create_tags(
    Resources=[
        'i-0d16fde49e71afcdc'
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'hopeworks'
        }
    ]
)
