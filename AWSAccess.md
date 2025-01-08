# Quick Start Guide: Accessing AWS

## 1. Sign into AWS Console (Web Interface)

Just visit [https://zindicomp.signin.aws.amazon.com/console](https://zindicomp.signin.aws.amazon.com/console) and sign in with your provided credentials. That's it! You're ready to use SageMaker and other AWS services.

## 2. Set Up Python Access (Optional)

If you want to access AWS from Python code (like in a Jupyter notebook), add this to your notebook:

```python
import boto3

# This will automatically use your credentials
s3 = boto3.client('s3')
sagemaker = boto3.client('sagemaker')
```

The credentials are already set up in your SageMaker environment - no extra configuration needed!

## 3. Command Line Access (Optional)

If you need to use the AWS command line (uncommon for this competition), run:

```bash
aws configure
```

And enter your credentials when prompted. The region should be `us-east-2`.

---
⚠️ Important: Never share your AWS credentials with anyone. They give access to your competition resources.
