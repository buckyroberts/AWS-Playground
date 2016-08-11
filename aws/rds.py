import boto3
from settings import *

client = boto3.client('rds')

response = client.create_db_instance(
    DBName=DB_NAME,
    DBInstanceIdentifier=DB_INSTANCE_ID,
    AllocatedStorage=ALLOCATED_STORAGE,
    DBInstanceClass=DB_INSTANCE_CLASS,
    Engine=ENGINE,
    MasterUsername=MASTER_USERNAME,
    MasterUserPassword=MASTER_USERPASSWORD,
    VpcSecurityGroupIds=VPC_SECURITY_GROUP_IDS,
    AvailabilityZone=AVAILABILITY_ZONE
)
