# AWS Resource Limits

The following limits apply to all competition participants:

## Compute Resources
- Maximum of 5 concurrent notebook instances
- Maximum of 20 vCPUs across all resources
- Instance types limited to:
  - ml.t3.medium ($0.05/hour)
    - 2 vCPU, 4 GiB memory
    - Good for development and testing
  - ml.t3.large ($0.10/hour)
    - 2 vCPU, 8 GiB memory
    - Better for memory-intensive tasks
  - ml.p3.2xlarge ($3.825/hour)
    - 8 vCPU, 61 GiB memory, 1 NVIDIA V100 GPU (16GB GPU RAM)
    - Best for deep learning training
  - ml.p3.8xlarge ($14.688/hour)
    - 32 vCPU, 244 GiB memory, 4 NVIDIA V100 GPUs (64GB total GPU RAM)
    - For large-scale training
  - ml.g4dn.2xlarge ($0.94/hour)
    - 8 vCPU, 32 GiB memory, 1 NVIDIA T4 GPU (16GB GPU RAM)
    - Good balance of CPU/GPU for mixed workloads
  - ml.g6.24xlarge ($7.344/hour)
    - 96 vCPU, 384 GiB memory, 4 NVIDIA A10G GPUs (96GB total GPU RAM)
    - High performance for large-scale training

Note: Spot instances are available at up to 70% discount from these prices.

## Batch Processing
- Default job configuration:
  - Memory: 32768MB (32GB)
  - vCPUs: 8
- Available instance types:
  - p3.2xlarge
  - p3.8xlarge
  - g4dn.2xlarge

## Storage
- S3 bucket storage: No explicit limit, but subject to cost budget
- EBS volumes: 
  - Default: 10GB
  - Maximum: 200GB per instance
- Space storage settings:
  - Default EBS volume size: 10GB
  - Maximum EBS volume size: 200GB

## SageMaker Studio Settings
- Auto-shutdown timeout: 120 minutes
- Minimum idle timeout: 60 minutes
- Maximum idle timeout: 360 minutes

## Budget
- Total budget: $400 USD
- Budget alerts at:
  - 80% ($320)
  - 100% ($400)
- When exceeded:
  - Running resources automatically stopped
  - New resource creation blocked
  - Email notifications sent to team and admin
  - Resources affected:
    - SageMaker instances
    - EC2 instances
    - Studio apps
