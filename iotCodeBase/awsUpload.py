import boto3
session = boto3.Session( #create session with keys, may need to be changed if outdated
    aws_access_key_id="*****************", #access key ID
    aws_secret_access_key="*******************", #Secret access key
)

s3 = session.client("s3")

s3.upload_file(
    Filename="/home/pi/Desktop/test.txt", #filepath of file you're uploading
    Bucket="cybersystemsandcomponentsproject", #bucket it's going in
    Key="cooltest.txt", #filename in bucket
)