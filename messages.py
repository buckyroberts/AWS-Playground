import boto3

sqs = boto3.resource('sqs')

# create the queue (this returns an SQS queue instance)
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# you can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
