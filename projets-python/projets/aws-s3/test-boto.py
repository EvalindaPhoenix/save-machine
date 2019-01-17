#!/usr/bin/python3
# A simple program to test boto and print s3 bucket names
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
