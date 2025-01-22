# Common ML Training Guidelines

For package installation instructions, see [Package Setup Guide](./guides/PackageSetup.md) and [Example Code](./examples/get_username.py).

## Best Practices

### Data Management

1. **Data Organization**

   - Keep raw data in separate S3 bucket/folder
   - Create processed data versions with clear naming
   - Document data preprocessing steps
   - Use data versioning when possible

2. **Efficient Data Loading**

   - Use data streaming for large datasets
   - Implement proper batching
   - Cache frequently used data
   - Use appropriate data formats (parquet for tabular, TFRecord for images)

3. **Data Validation**
   - Check for missing values
   - Validate data types
   - Monitor data distributions
   - Test data pipeline components

### Model Development

1. **Code Organization**

   - Use modular code structure
   - Create reusable components
   - Document functions and classes
   - Use version control

2. **Training Best Practices**

   - Start with small dataset for testing
   - Implement early stopping
   - Use learning rate scheduling
   - Monitor training metrics
   - Save checkpoints regularly
   - Log experiments
   - Use spot instances when possible (up to 70% cost savings)

3. **Resource Management**
   - Monitor GPU memory usage
   - Use mixed precision training
   - Clean up unused resources
   - Schedule automatic shutdowns
   - Choose cost-effective instance types (see aws-pricing/instance_pricing.md)

### Common ML Container Images

The following container images are available in us-east-2 for ML training and inference:

1. **PyTorch**

   ```python
   # Latest PyTorch with GPU support
   pytorch_image = '763104351884.dkr.ecr.us-east-2.amazonaws.com/pytorch-training:2.0.0-gpu-py310'
   ```

2. **TensorFlow**

   ```python
   # Latest TensorFlow with GPU support
   tensorflow_image = '763104351884.dkr.ecr.us-east-2.amazonaws.com/tensorflow-training:2.12.1-gpu-py39'
   ```

3. **Hugging Face**

   ```python
   # Latest Hugging Face with PyTorch
   huggingface_pytorch = '763104351884.dkr.ecr.us-east-2.amazonaws.com/huggingface-pytorch-training:4.26.0-gpu-py310'
   ```

Example usage with SageMaker:

```python
import sagemaker
from sagemaker.estimator import Estimator

estimator = Estimator(
    image_uri='763104351884.dkr.ecr.us-east-2.amazonaws.com/pytorch-training:2.0.0-gpu-py310',
    role=sagemaker.get_execution_role(),
    instance_count=1,
    instance_type='ml.p3.2xlarge'
)
```

### AWS Resource Usage

1. **Region & Tagging Requirements**

   - All resources MUST be in **US East (Ohio) / us-east-2**
   - Every resource MUST be tagged with `team = <your-username>`
   - See [Resource Tagging Requirements](./TaggingRequirements.md)

2. **AWS Batch Job Queues**

   - Only these three regional compute queues are available:
     - main-compute-queue-us-east-2a
     - main-compute-queue-us-east-2b
     - main-compute-queue-us-east-2c
   - Submit jobs to the queue matching your availability zone
   - No other compute queues are available

3. **Cost Optimization**

   - Use spot instances when possible
   - Monitor resource usage in [Cost Dashboard](./CostMonitoring.md)
   - Set up budget alerts
   - Clean up unused endpoints
   - Stay within [Resource Limits](./ResourceLimits.md)

4. **Storage Management**
   - Use appropriate storage classes
   - Clean up old checkpoints
   - Compress data when possible
   - Use lifecycle policies

## CloudWatch Monitoring

### Setting Up Monitoring

1. Create custom dashboards for:

   - Training metrics
   - Resource utilization
   - Cost tracking
   - Job status

2. Configure alerts for:
   - Training completion
   - Error conditions
   - Resource limits
   - Cost thresholds

### Accessing Logs

1. **Console Access**

   - Navigate to CloudWatch
   - Select Log groups
   - Filter by resource type:
     - `/aws/sagemaker/NotebookInstances/<notebook-name>`
     - `/aws/sagemaker/TrainingJobs/<job-name>`
     - `/aws/sagemaker/Endpoints/<endpoint-name>`

2. **CLI Access**

```bash
# Get recent logs
aws logs get-log-events \
    --log-group-name /aws/sagemaker/NotebookInstances/<notebook-name> \
    --log-stream-name <stream-name>

# Filter logs
aws logs filter-log-events \
    --log-group-name /aws/sagemaker/TrainingJobs/<job-name> \
    --filter-pattern "ERROR"
```

## Troubleshooting Guide

### Environment Issues

1. **Wrong Region**

   - Verify region is us-east-2 (Ohio)
   - Check AWS_DEFAULT_REGION
   - Update boto3 session region

2. **Package Conflicts**
   - Use virtual environments
   - Check package versions
   - Clear pip cache if needed
   - Review dependency conflicts

### Training Problems

1. **Memory Issues**

   - Monitor memory usage
   - Reduce batch size
   - Enable gradient checkpointing
   - Use mixed precision training
   - Clean up unused variables

2. **Performance Issues**

   - Profile code execution
   - Optimize data loading
   - Use appropriate instance types
   - Monitor GPU utilization
   - Check I/O bottlenecks

3. **Convergence Problems**
   - Check learning rate
   - Validate loss function
   - Monitor gradients
   - Inspect data quality
   - Test simpler models first

### Access Issues

1. **Permission Errors**

   - Verify IAM roles
   - Check bucket policies
   - Review security groups
   - Test with minimal permissions
   - Use AWS Policy Simulator

2. **Network Problems**
   - Check VPC configuration
   - Verify endpoint access
   - Test network connectivity
   - Monitor network metrics

### Resource Management

1. **Quota Limits**

   - Monitor service quotas
   - Request limit increases
   - Use resource scheduling
   - Implement retry logic

2. **Cost Control**
   - Set up budget alerts
   - Monitor usage patterns
   - Use auto-shutdown
   - Clean up resources
   - Optimize instance selection

## Getting Help

1. **Documentation**

   - AWS Documentation
   - SageMaker Examples
   - Framework Guides
   - Community Resources

2. **Support Channels**

   - AWS Support
   - Competition Forums
   - GitHub Issues
   - Stack Overflow

3. **Debugging Tools**
   - SageMaker Debugger
   - TensorBoard
   - Python Debugger
   - CloudWatch Insights
