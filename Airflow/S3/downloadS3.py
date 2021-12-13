import boto3

# address to download the relevant data
raw_path = 'C:/Users/yunus/OneDrive/Masaüstü/Brazillian ECommerce/myprojectecommerce/Data/'

# Determination of the relevant structure as a customer through the library
s3 = boto3.client('s3')
# Example -> S3

#Functionally, the bucket_name is the structure that downloads the data by taking the file name and extension to be downloaded.
s3.download_file('myprojectecommerce', 'archive.zip', raw_path)

