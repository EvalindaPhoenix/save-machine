import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call to S3 to retrieve the policy for the given bucket
result = s3.get_bucket_acl(Bucket='emilie-test-s3-pdm-ftc')
print(result)

