import boto3

ec2 = boto3.resource('ec2')
key_pair = ec2.KeyPair('dev-08-07-2016')

print(key_pair.key_name)
print(key_pair.key_fingerprint)

# note: when deleted, the key_name still exists but the fingerprint does not
# attempting to delete again will throw an "InvalidKeyPair.NotFound" error
key_pair.delete()
