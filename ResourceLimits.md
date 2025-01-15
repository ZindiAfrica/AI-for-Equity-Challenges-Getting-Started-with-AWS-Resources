# AWS Resource Limits

The following limits apply to all competition participants:

## Compute Resources
- Maximum of 5 concurrent notebook instances
- Maximum of 20 vCPUs across all resources
- Instance types limited to:

### SageMaker Training Instances

#### General Purpose (M5)
  - ml.m5.large ($0.096/hour on-demand, $0.0288/hr spot)
    - 2 vCPU, 8 GiB memory
  - ml.m5.xlarge ($0.672/hour on-demand, $0.2016/hr spot)
    - 4 vCPU, 16 GiB memory
  - ml.m5.2xlarge ($0.519/hour on-demand, $0.1557/hr spot)
    - 8 vCPU, 32 GiB memory
  - ml.m5.4xlarge ($6.768/hour on-demand, $2.0304/hr spot)
    - 16 vCPU, 64 GiB memory

#### Memory Optimized (R5)
  - ml.r5.2xlarge ($1.464/hour on-demand, $0.4392/hr spot)
    - 8 vCPU, 64 GiB memory
  - ml.r5.4xlarge ($2.928/hour on-demand, $0.8784/hr spot)
    - 16 vCPU, 128 GiB memory
  - ml.r5.8xlarge ($5.856/hour on-demand, $1.7568/hr spot)
    - 32 vCPU, 256 GiB memory

#### GPU Instances (G4DN)
  - ml.g4dn.4xlarge ($1.204/hour on-demand, $0.3612/hr spot)
    - 16 vCPU, 64 GiB memory, 1 NVIDIA T4 GPU
  - ml.g4dn.8xlarge ($2.176/hour on-demand, $0.6528/hr spot)
    - 32 vCPU, 128 GiB memory, 1 NVIDIA T4 GPU

### AWS Batch Compute Instances

#### GPU Instances
  - p3.2xlarge ($3.06/hour on-demand, $0.918/hr spot)
    - 8 vCPU, 61 GiB memory, 1 NVIDIA V100 GPU
  - p3.8xlarge ($12.24/hour on-demand, $3.672/hr spot) 
    - 32 vCPU, 244 GiB memory, 4 NVIDIA V100 GPUs
  - g4dn.2xlarge ($0.752/hour on-demand, $0.226/hr spot)
    - 8 vCPU, 32 GiB memory, 1 NVIDIA T4 GPU

Note: Additional instance types may be requested but approval will be at the organizers' discretion based on availability and requirements.

Note: Spot instances can provide up to 70% cost savings compared to On-Demand pricing.

## AWS Batch Processing
- Default job configuration:
  - Memory: 32768MB (32GB)
  - vCPUs: 8
- Available Compute Queues (Only):
  - main-compute-queue-us-east-2a
  - main-compute-queue-us-east-2b 
  - main-compute-queue-us-east-2c
- Available Compute Instance Types (Only):
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
