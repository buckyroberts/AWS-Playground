import boto3

s3 = boto3.resource('s3')

# creating a bucket
s3.create_bucket(Bucket='uniqueBucketName')

# print out all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# storing data
s3.Object('uniqueBucketName', 'sample.txt').put(Body=open('sample.txt', 'rb'))

for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        print(key.key)
