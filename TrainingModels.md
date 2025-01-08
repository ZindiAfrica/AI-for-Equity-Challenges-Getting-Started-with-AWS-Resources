# Training Models on AWS

## Overview

This guide explains the different options and best practices for training machine learning models using AWS services in this competition.

## Using SageMaker for Training

1. In the SageMaker dashboard, click on **Training jobs** in the left-hand navigation pane.
2. Click on the **Create training job** button.
3. Enter a name for your training job.
4. Select the training algorithm (e.g., `XGBoost`).
5. Specify the S3 location of your training data.
6. Select an instance type (e.g., `ml.m5.large`).
7. For the IAM role, choose the role created by the Terraform script (e.g., `MySageMakerExecutionRole`).
8. Click on the **Create training job** button.

## Best Practices

1. Start with small datasets on SageMaker for development
2. Use checkpointing to save progress regularly
3. Monitor resource usage via CloudWatch
4. Consider using Spot instances for cost savings
5. Clean up resources after training completes

## Resource Limits

Remember these limits when planning your training:
- Maximum 20 vCPUs across all resources
- Available instance types: ml.t3.medium, ml.t3.large, ml.p3.2xlarge, ml.p3.8xlarge, ml.g4dn.2xlarge
- GPU instances only available in EC2-based queue
