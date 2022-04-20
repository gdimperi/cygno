import boto3
from boto3sts import credentials as creds
import pandas as pd

aws_session = creds.assumed_session("infncloud-iam")
s3 = aws_session.client('s3', endpoint_url="https://minio.cloud.infn.it/", config=boto3.session.Config(signature_version='s3v4'),verify=True)
response = s3.list_objects(Bucket='cygno-data')['Contents']
for i, file in enumerate(response):
    print(file['Key'], file['LastModified'])
#file_db = pd.read_json(file_list)
#print (file_db)
