import boto3
from boto3.s3.transfer import S3Transfer
import os

access_key = 'AKIATRF5USIJR3IQQXP7'
secret_key = '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'
s3_bucket_name = 'myprojectecommerce'
s3_filename = 'achive.zip'
s3_filename = 'achive.csv'
client = boto3.client('s3',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)

print('client')

transfer = S3Transfer(client)

print('Transfer - ' + s3_bucket_name)


def upload(path, s3_bucket_name):
    for root, dirs, files in os.walk(path):
        for file in files:

            if file.endswith('csv'):
                transfer.upload_file(os.path.join(root, file),
                                     s3_bucket_name, + file)


filepath = "C:\\Users\\yunus\\OneDrive\\Masaüstü\\Brazillian ECommerce\\myprojectecommerce\\Kaggle - Data"
upload(path=filepath, s3_bucket_name='myprojectecommerce')
