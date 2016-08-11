# IAM
USERNAME = 'tommy'
POLICY_ARN = 'arn:aws:iam::aws:policy/AdministratorAccess'

# EC2
IMAGE_ID = 'ami-d732f0b7'
INSTANCE_NAMES = {'web server 1', 'web server 2'}
INSTANCE_TYPE = 't2.micro'

# RDS
ALLOCATED_STORAGE = 5
AVAILABILITY_ZONE = 'us-west-2a'
DB_NAME = 'sample_db_2'
DB_INSTANCE_CLASS = 'db.t1.micro'
DB_INSTANCE_ID = 'sample-db-instance-2'
ENGINE = 'mysql'
MASTER_USERNAME = 'admin'
MASTER_USERPASSWORD = 'pass1234'
VPC_SECURITY_GROUP_IDS = ['sg-e190b987']
