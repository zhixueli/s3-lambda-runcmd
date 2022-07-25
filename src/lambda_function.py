import boto3
import botocore
import time
import os

def lambda_handler(event, context):
    
    statusCode = 200
    sourceS3Bucket = event['Records'][0]['s3']['bucket']['name']
    sourceS3Key = event['Records'][0]['s3']['object']['key']
    sourceS3 = 's3://'+ sourceS3Bucket + '/' + sourceS3Key
    
    client = boto3.client('ssm')

    instance_id = os.environ['InstanceID']
    
    try:
        response = client.send_command(
            InstanceIds=[instance_id],
            DocumentName='AWS-RunShellScript',
            Parameters={
                'commands': [
                    # Simple test if a file exists
                    'aws s3 cp ' + sourceS3 + ' /home/ec2-user/'
                ]
            }
        )
    
    except Exception as e:
        print('Exception: %s' % e)
        statusCode = 500
    
    finally:
        return statusCode
