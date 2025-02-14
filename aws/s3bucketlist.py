import boto3

print("Starting with low level CLIENT to S3")
session = boto3.session.Session(profile_name='iamadmin-production')
client = session.client('s3')

response = client.list_buckets()
print("The data type of the response was")
print(type(response))

# This is the original, lower level call
# This uses the client connection which has 100% service API coverage e.g. list_buckets() => S3ListBucket service API
# We get a dict back from the call

# If we use the resource connection (resource is higher, like ORM)
# We get a collection provides an iterable interface to a group of resources.
# Read https://boto3.amazonaws.com/v1/documentation/api/latest/guide/collections.html

# s3 = boto3.resource('s3', aws_access_key_id='', aws_secret_access_key='')

print("Starting with high level RESOURCE to S3")
session = boto3.session.Session(profile_name='iamadmin-production')
s3 = session.resource('s3')

print("Starting loop over buckets")
for bucket in s3.buckets.all():
    print(bucket.name)

buckets = list(s3.buckets.all())
print(type(buckets))
print(buckets)

try:
    s3.head_bucket(Bucket='hodei-veeama')
    raise SystemExit('This bucket has already been created')
except botocore.exceptions.ClientError as e:
    error_code = int(e.response['Error']['Code'])
    print('Existing Bucket Not Found,please proceed to create one with this name')


#response2 =
#print(response2)
#print(type(response2))
