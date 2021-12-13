import boto3

raw_path = 'C:/Users/yunus/OneDrive/Masaüstü/Brazillian ECommerce/myprojectecommerce/Data/'
s3 = boto3.client('s3')
s3.download_file('myprojectecommerce', 'archive.zip', raw_path)