import boto3

ec2 = boto3.resource('ec2')
security_group = ec2.SecurityGroup('sg-e190b987')

print(security_group.description)
print(security_group.group_id)
print(security_group.group_name)

print('\nIP Permissions:')
for permission in security_group.ip_permissions:
    for p in permission:
        print(p + ' - ' + str(permission[p]))
