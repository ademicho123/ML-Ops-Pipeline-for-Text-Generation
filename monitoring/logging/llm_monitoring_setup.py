import boto3
from botocore.exceptions import NoCredentialsError

def setup_monitoring_and_logging():
    # CloudWatch and CloudTrail clients Set up
    cloudwatch = boto3.client('cloudwatch')
    cloudtrail = boto3.client('cloudtrail')

    # CloudWatch metric for monitoring 
    cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName': 'ModelLatency',
                'Dimensions': [
                    {
                        'Name': 'LLM Model',
                        'Value': 'YourModel',
                    },
                ],
                'Unit': 'Milliseconds',
                'Value': 50,
            },
        ],
        Namespace='YourNamespace',
    )

    # Set up CloudTrail for logging
    response = cloudtrail.create_trail(
        Name='YourTrail',
        S3BucketName='your-s3-logging-bucket',
    )

    # Start the CloudTrail trail
    cloudtrail.start_logging(Name='YourTrail')

    # Set up QuickSight for visualization (example)
    quicksight = boto3.client('quicksight')

    response = quicksight.create_data_source(
        AwsAccountId='your-aws-account-id',
        DataSourceId='YourDataSource',
        Name='YourDataSource',
        Type='S3',
        DataSourceParameters={
            'S3Parameters': {
                'ManifestFileLocation': {
                    'Bucket': 'your-s3-logging-bucket', 
                    'Key': 'quicksight-manifest.json',
                },
            },
        },
        Permissions=[
            {
                'Principal': 'arn:aws:quicksight:your-region:your-aws-account-id:user/default/your-username',
                'Actions': ['quicksight:DescribeDataSource'],
            },
        ],
    )

    print("Monitoring, logging, and QuickSight configuration completed successfully.")

if __name__ == "__main__":
    try:
        setup_monitoring_and_logging()
    except NoCredentialsError:
        print("AWS credentials not available.")
