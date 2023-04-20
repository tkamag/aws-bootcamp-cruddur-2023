import boto3
import json
from pprint import pprint

iam_client = boto3.client('iam',
        aws_access_key_id='${AWS_ACCESS_KEY_ID}',
        aws_secret_access_key='${AWS_SECRET_ACCESS_KEY}')

assume_policy = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                    "redshift.amazonaws.com"
                ]
            }
        }
    ]
})

response = iam_client.create_role(
    RoleName='myRedshiftRole',
    AssumeRolePolicyDocument=assume_policy)

print(response["Role"]["RoleName"])

resp = iam_client.attach_role_policy(
    RoleName='myRedshiftRole',
        PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)

pprint(resp)
#print(json.loads(response))
