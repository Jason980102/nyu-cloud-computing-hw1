# nyu-cloud-computing-hw1

# NYU Cloud Computing HW1 (EC2 + S3 using IAM Role)

This repository demonstrates an AWS EC2 instance accessing Amazon S3 using an IAM Role 
(without storing AWS credentials in code)

## Environment
- EC2 OS: SUSE Linux Enterprise Server 16
- Python: 3.13
- AWS SDK: boto3

## Application Description
The Python application performs the following steps:
1. Uses the IAM role attached to the EC2 instance (`cc-hw1-ec2-s3-role`)
2. Uploads a text file to an Amazon S3 bucket
3. Reads the uploaded file back from S3 and prints the content

## How to Run
```bash
python3.13 app.py
