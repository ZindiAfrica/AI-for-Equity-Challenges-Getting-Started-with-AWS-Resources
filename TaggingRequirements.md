# Resource Tagging Requirements

When working in the AWS environment, it is **mandatory** to tag all resources you create with your team identifier. This helps with cost tracking, resource management, and security compliance.

## Required Tag

All resources MUST include the following tag:

```
team = <your-username>
```

For example, if your username is "team-alpha", all resources you create should be tagged with:

```
team = team-alpha
```

## Resources That Need Tagging

You must apply this tag to all resources you create, including but not limited to:

- SageMaker notebooks, training jobs, and endpoints
- S3 buckets and objects
- Batch compute jobs
- CloudWatch log groups
- Any other AWS resources you create

## How to Apply Tags

### In SageMaker Studio

When creating resources through SageMaker Studio, ensure you:

1. Expand the "Tags" section in creation forms
2. Click "Add new tag"
3. Enter "team" as the Key
4. Enter your username as the Value

### Using AWS CLI

When using AWS CLI, add the --tags parameter:

```
aws sagemaker create-training-job \
  --training-job-name my-training-job \
  --tags Key=team,Value=<your-username> \
  ...
```

### Using AWS SDK

When using AWS SDKs, include tags in your resource creation calls:

```python
sagemaker.create_training_job(
    TrainingJobName='my-training-job',
    Tags=[{'Key': 'team', 'Value': '<your-username>'}],
    ...
)
```

## Important Notes

- Resources without proper tags may be automatically terminated
- Cost tracking and budgeting are based on these tags
- Security policies and access controls use these tags
- Regular audits will check for proper tagging compliance

## Need Help?

If you're unsure about tagging or encounter any issues, please contact the competition administrators.
