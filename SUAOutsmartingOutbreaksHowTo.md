# SUA Outsmarting Outbreaks Challenge - How To Guide

For instructions on accessing AWS services including console login, CLI setup, and SDK configuration, please see [AWS Access Guide](./AWSAccess.md).

## Using SageMaker

For detailed instructions on using SageMaker, including training options, deploying models, and troubleshooting, please see [Using SageMaker](./UsingSageMaker.md).

For information about cost monitoring, budgets and resource limits, please see:
- [Cost Monitoring Guide](./CostMonitoring.md)
- [Resource Limits](./ResourceLimits.md)

## Accessing Competition Data

1. Navigate to **S3** in the AWS Console
2. Each user/team has a private bucket named `<username>-team-bucket` (e.g., `comp-user-jvlemq-team-bucket`) for storing your work
3. The competition data is available in two regions:

   **US East (Ohio) - Recommended**
   - Bucket: `sua-outsmarting-outbreaks-challenge-comp` (us-east-2)
   - Use this bucket for faster access from SageMaker

   **Europe (London)**
   - Bucket: `sua-outsmarting-outbreaks-challenge` (eu-west-2)
   - Alternative access point

   Access the US East bucket (recommended) using:
   ```python
   import boto3
   
   # Access the public bucket directly
   s3 = boto3.client('s3', region_name='us-east-2')
   
   # List contents
   response = s3.list_objects_v2(Bucket='sua-outsmarting-outbreaks-challenge-comp')
   ```
   
   The bucket contains:
   - `OutsmartingOutbreaks_StarterNotebook.ipynb`: Starter notebook with example code
   - `SampleSubmission.csv`: Example submission file format
   - `Test.csv`: Test dataset for predictions
   - `Train.csv`: Training dataset
   - `VariableDefinitions.txt`: Descriptions of dataset variables
   - `toilets.csv`: Toilet facility locations and information
   - `waste_management.csv`: Waste management site data
   - `water_sources.csv`: Water source locations and details
4. You can access this data directly from your notebook or Batch jobs

## Additional Resources

- [SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
- [S3 Documentation](https://docs.aws.amazon.com/s3/)
- [CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
