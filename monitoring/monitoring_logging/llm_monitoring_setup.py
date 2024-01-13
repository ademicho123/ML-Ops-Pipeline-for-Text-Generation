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
                        'Name': 'LLM Model',                # Update with the right info
                        'Value': 'YourModel',               # Update with the right info
                    },
                ],
                'Unit': 'Milliseconds',
                'Value': 50,
            },
        ],
        Namespace='YourNamespace',                         # Update with the right info
    )

    # Set up CloudTrail for logging
    response = cloudtrail.create_trail(
        Name='YourTrail',                                  # Update with the right info
        S3BucketName='your-s3-logging-bucket',             # Update with the right info
    )

    # Start the CloudTrail trail
    cloudtrail.start_logging(Name='YourTrail')              # Update with the right info

    # QuickSight for visualization Set up
    quicksight = boto3.client('quicksight')

    response = quicksight.create_data_source(
        AwsAccountId='your-aws-account-id',                     # Update with the right info
        DataSourceId='YourDataSource',                          # Update with the right info
        Name='YourDataSource',                                  # Update with the right info
        Type='S3',
        DataSourceParameters={
            'S3Parameters': {
                'ManifestFileLocation': {
                    'Bucket': 'your-s3-logging-bucket',         # Update with the right info
                    'Key': 'quicksight-manifest.json',          # Update with the right info
                },
            },
        },
        Permissions=[
            {
                'Principal': 'arn:aws:quicksight:your-region:your-aws-account-id:user/default/your-username',       # Update with the right info 
                'Actions': ['quicksight:DescribeDataSource'],                                                       # Update with the right info
            },
        ],
    )

    print("Monitoring, logging, and QuickSight configuration completed successfully.")

if __name__ == "__main__":
    try:
        setup_monitoring_and_logging()
    except NoCredentialsError:
        print("AWS credentials not available.")
