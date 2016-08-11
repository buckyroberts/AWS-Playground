import boto3

ec2 = boto3.resource('ec2')

# create a new instance
ec2.create_instances(ImageId='ami-3e32f05e', MinCount=1, MaxCount=1)

# check what instances are running
for instance in ec2.instances.all():
    print(instance.id, instance.instance_type)

# filter instances
for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
    print(instance.id, instance.instance_type)

# start, stop, and terminate instance by ID
# ec2.instances.filter(InstanceIds=['i-sampleId']).start()
# ec2.instances.filter(InstanceIds=['i-sampleId']).stop()
# ec2.instances.filter(InstanceIds=['i-sampleId']).terminate()

for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)
