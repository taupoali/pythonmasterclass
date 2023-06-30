import boto3

client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
response = client.list_buckets()
print(type(response))

# This is the original, lower level call
# This uses the client connection which has 100% service API coverage e.g. list_buckets() => S3ListBucket service API
# We get a dict back from the call


# If we use the resource connection
# We get a collection provides an iterable interface to a group of resources.
# Read https://boto3.amazonaws.com/v1/documentation/api/latest/guide/collections.html

s3 = boto3.resource('s3', aws_access_key_id='', aws_secret_access_key='')
for bucket in s3.buckets.all():
    print(bucket.name)

buckets = list(s3.buckets.all())
print(type(buckets))
print(buckets)