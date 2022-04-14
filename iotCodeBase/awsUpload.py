import boto3
session = boto3.Session( #create session with keys, may need to be changed if outdated
    aws_access_key_id="AKIAW3T63HVT24D5MC3", #access key ID
    aws_secret_access_key="FO0z6yQhkAeRjFha+BpESM6AXI1JMFsp2kTSUpV2", #Secret access key
)

s3 = session.client("s3")

s3.upload_file(
    Filename="/home/pi/Desktop/test.txt", #filepath of file you're uploading
    Bucket="cybersystemsandcomponentsproject", #bucket it's going in
    Key="cooltest.txt", #filename in bucket
)