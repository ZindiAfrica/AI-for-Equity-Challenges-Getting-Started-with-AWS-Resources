# Kuyesera AI Disaster Damage and Displacement Challenge - How To Guide

For instructions on accessing AWS services including console login, CLI setup, and SDK configuration, please see [AWS Access Guide](./AWSAccess.md).

## Opening SageMaker Studio

1. In the AWS Console, navigate to SageMaker
2. Click "Studio" in the left navigation menu
3. Select your domain and user profile
4. Click "Open Studio"
5. Wait for Studio to load - you'll see the JupyterLab interface

## Using SageMaker

For detailed instructions on using SageMaker, including training options, deploying models, and troubleshooting, please see [Using SageMaker](./UsingSageMaker.md).

For information about cost monitoring, budgets and resource limits, please see:

- [Cost Monitoring Guide](./CostMonitoring.md)
- [Resource Limits](./ResourceLimits.md)

## Accessing Data in S3 Buckets

1. In the AWS Management Console, navigate to the **S3** service.
2. Each user/team has a private bucket named `<username>-team-bucket` (e.g., `comp-user-jvlemq-team-bucket`) for storing your work.
3. The competition data is available in two regions:

   **US East (Ohio) - Recommended**

   - Bucket: `kuyesera-ai-challenge-comp` (us-east-2)
   - Use this bucket for faster access from SageMaker

   **Europe (London)**

   - Bucket: `kuyesera-ai-challenge` (eu-west-2)
   - Alternative access point

   Access the US East bucket (recommended) using:

   ```python
   import boto3

   # Access the public bucket directly
   s3 = boto3.client('s3', region_name='us-east-2')

   # List contents
   response = s3.list_objects_v2(Bucket='kuyesera-ai-challenge-comp')
   ```

4. The bucket contains the following files:

   - `SampleSubmission.csv` (53.7 KB): Example submission file format
   - `Starter Notebook Kuyesera.ipynb` (15.5 MB): Starter notebook with example code
   - `test_image_coords.csv` (119.9 KB): Test dataset coordinates
   - `test_images.zip` (723.2 MB): Test dataset images
   - `xview2_geotiff.tgz`: Training dataset from xBD
   - `SampleSubmission.csv` (53.7 KB): Example submission file format
   - `Starter Notebook Kuyesera.ipynb` (15.5 MB): Starter notebook with example code
   - `test_image_coords.csv` (119.9 KB): Test dataset coordinates
   - `test_images.zip` (723.2 MB): Test dataset images
   - `xview2_geotiff.tgz`: Training dataset from xBD

5. You can download the data files to your local machine or use them directly in your SageMaker notebook instance.

## Analyzing Data and Training Models

1. Open your SageMaker notebook instance.
2. Upload the data files from the S3 bucket to your notebook instance.
3. Use Python and popular data analysis libraries such as Pandas, NumPy, and Matplotlib to analyze the data.
4. Use machine learning libraries such as Scikit-learn, TensorFlow, or PyTorch to train your models.
5. Save your trained models to the S3 bucket for later use.

## Accessing CloudWatch Logs

To view logs from your training jobs and notebooks:

1. Navigate to CloudWatch in the AWS Console
2. Click "Log groups" in the left navigation
3. Find your logs:
   - SageMaker logs: `/aws/sagemaker/NotebookInstances/<notebook-name>`
   - Training logs: `/aws/sagemaker/TrainingJobs/<job-name>`

You can also access logs via AWS CLI:

```bash
aws logs get-log-events --log-group-name <log-group> --log-stream-name <stream>
```

## Troubleshooting

Common issues and solutions:

1. **Wrong Region Selected**

   - Ensure you're in US East (Ohio) region (us-east-2)
   - Check region selector in top-right of AWS Console
   - All competition resources are in us-east-2

2. **Memory Issues During Training**

   - Monitor memory usage in CloudWatch
   - Reduce batch size
   - Use instance with more memory
   - Enable memory optimization flags

3. **Access Denied Errors**

   - Verify correct IAM role usage
   - Check bucket permissions
   - Review security group settings

4. **Resource Creation Failed**

   - Check budget status
   - Verify resource quotas
   - Review CloudWatch logs

5. **Data Loading Issues**
   - Verify S3 paths are correct
   - Check data format compatibility
   - Monitor network performance

## Additional Resources

- [Amazon SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/index.html)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/index.html)
- [AWS Console Login](https://zindicomp.signin.aws.amazon.com/console)
- [CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
