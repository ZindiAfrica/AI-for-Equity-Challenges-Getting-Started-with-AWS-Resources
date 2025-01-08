# Using SageMaker for Model Training

See [Common ML Training Guidelines](./MLTrainingCommon.md) for setup and best practices.

## Example Code

Here's an example of how to use SageMaker for development and training:

```python
import boto3
import sagemaker
from sagemaker.session import Session

# Initialize SageMaker session
sagemaker_session = Session()

# 1. Development in SageMaker Notebook
def develop_model():
    # Test model on small dataset
    import pandas as pd
    import numpy as np
    
    # Use global BUCKET_NAME 
    global BUCKET_NAME
    
    # Load sample data
    df = pd.read_csv(f's3://{BUCKET_NAME}/examples/sample_data.csv')
    
    # Develop model
    def train_model(df):
        # Your model training logic here
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()
        model.fit(df[features], df[target])
        return model
    
    # Test on small sample
    model = train_model(df)
    return model

# 2. Train model in SageMaker
def train_model():
    # Get SageMaker execution role
    role = sagemaker.get_execution_role()
    
    estimator = sagemaker.estimator.Estimator(
        image_uri='763104351884.dkr.ecr.us-east-2.amazonaws.com/pytorch-training:2.5.1-gpu-py311-cu124-ubuntu22.04-sagemaker',
        role=role,
        instance_count=1,
        instance_type='ml.p3.2xlarge',
        output_path=f's3://{BUCKET_NAME}/model-output/',
        max_run=86400
    )
    
    # Set hyperparameters
    estimator.set_hyperparameters(
        epochs=50,
        batch_size=128,
        learning_rate=0.001
    )
    
    # Start training
    estimator.fit({
        'training': f's3://{BUCKET_NAME}/processed/train',
        'validation': f's3://{BUCKET_NAME}/processed/validation'
    })

# Get bucket name based on role
def get_bucket_name():
    import boto3
    import re
    sts = boto3.client('sts')
    caller_identity = sts.get_caller_identity()
    role_arn = caller_identity['Arn']
    
    # Extract username from role ARN
    match = re.search(r'SageMakerRole-team-([\w-]+)', role_arn)
    if not match:
        raise ValueError("Could not extract username from role ARN")
    username = match.group(1)
    return f"{username}-bucket"

# Example workflow
if __name__ == "__main__":
    # Get bucket name first
    BUCKET_NAME = get_bucket_name()
    
    # 1. Develop and test model
    model = develop_model()
    print("Model development completed")
    
    # 2. Train full model in SageMaker
    train_model()
    print("Model training completed")
```

## Key Points:

1. Development in SageMaker:
   - Use SageMaker notebooks for development and testing
   - Test on small data samples
   - Iterate quickly on model architecture

2. Model Training in SageMaker:
   - Use processed data from development
   - Leverage GPU instances for training
   - Monitor training progress in SageMaker console

## Running the Example:

1. Save this code in a SageMaker notebook
2. Configure AWS credentials and roles
3. Update S3 paths and role ARNs
4. Execute cells to test workflow

Remember to check [Common ML Training Guidelines](./MLTrainingCommon.md) for:
- Package installation
- Best practices
- Troubleshooting
- CloudWatch logging
