import boto3

url = boto3.client('s3').generate_presigned_url(ClientMethod='get_object', Params={'Bucket': 'hodei-videos', 'Key':'demo-complaint_01.mp3'},ExpiresIn=3600)
print("The generated url is " + url)
