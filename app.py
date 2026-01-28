import boto3

BUCKET_NAME = "cc-hw1-jc14531-nyu"   
OBJECT_KEY = "app-output/hello.txt"

def main():
    s3 = boto3.client("s3")

    message = "Hello from EC2 Python application using IAM Role!\n"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=OBJECT_KEY,
        Body=message.encode("utf-8")
    )

    print(f"[OK] Uploaded object to s3://{BUCKET_NAME}/{OBJECT_KEY}")

    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=OBJECT_KEY
    )

    content = response["Body"].read().decode("utf-8")

    print("[OK] Read back content from S3:")
    print("--------------------------------")
    print(content)
    print("--------------------------------")

if __name__ == "__main__":
    main()
