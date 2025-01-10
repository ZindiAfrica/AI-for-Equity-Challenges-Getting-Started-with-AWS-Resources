# AWS Resource Limits

The following limits apply to all competition participants:

## Compute Resources
- Maximum of 5 concurrent notebook instances
- Maximum of 20 vCPUs across all resources
- Instance types limited to:

### General Purpose (T3/T3A)
  - ml.t3.medium ($0.05/hour on-demand, $0.015/hr spot)
    - 2 vCPU, 4 GiB memory
    - Best for development and testing
  - ml.t3.large ($0.10/hour on-demand, $0.03/hr spot)
    - 2 vCPU, 8 GiB memory
  - ml.t3.xlarge ($0.20/hour on-demand, $0.06/hr spot)
    - 4 vCPU, 16 GiB memory
  - ml.t3a.xlarge ($0.18/hour on-demand, $0.054/hr spot)
    - 4 vCPU, 16 GiB memory (AMD)
  - ml.t3.2xlarge ($0.40/hour on-demand, $0.12/hr spot)
    - 8 vCPU, 32 GiB memory
  - ml.t3a.2xlarge ($0.36/hour on-demand, $0.108/hr spot)
    - 8 vCPU, 32 GiB memory (AMD)

### Memory Optimized (R5/R5A)
  - ml.r5.large ($0.15/hour on-demand, $0.045/hr spot)
    - 2 vCPU, 16 GiB memory
  - ml.r5.xlarge ($0.30/hour on-demand, $0.09/hr spot)
    - 4 vCPU, 32 GiB memory
  - ml.r5.2xlarge ($0.60/hour on-demand, $0.18/hr spot)
    - 8 vCPU, 64 GiB memory
  - ml.r5a.2xlarge ($0.54/hour on-demand, $0.162/hr spot)
    - 8 vCPU, 64 GiB memory (AMD)
  - ml.r5.4xlarge ($1.20/hour on-demand, $0.36/hr spot)
    - 16 vCPU, 128 GiB memory

### GPU Instances (G4DN/G4AD)
  - ml.g4dn.xlarge ($0.736/hour on-demand, $0.221/hr spot)
    - 4 vCPU, 16 GiB memory, 1 NVIDIA T4 GPU
  - ml.g4dn.2xlarge ($0.90/hour on-demand, $0.27/hr spot)
    - 8 vCPU, 32 GiB memory, 1 NVIDIA T4 GPU
  - ml.g4dn.4xlarge ($1.43/hour on-demand, $0.429/hr spot)
    - 16 vCPU, 64 GiB memory, 1 NVIDIA T4 GPU
  - ml.g4dn.8xlarge ($2.72/hour on-demand, $0.816/hr spot)
    - 32 vCPU, 128 GiB memory, 1 NVIDIA T4 GPU

### High-Performance GPU (P3)
  - ml.p3.2xlarge ($3.06/hour on-demand, $0.918/hr spot)
    - 8 vCPU, 61 GiB memory, 1 NVIDIA V100 GPU
  - ml.p3.8xlarge ($12.24/hour on-demand, $3.672/hr spot)
    - 32 vCPU, 244 GiB memory, 4 NVIDIA V100 GPUs

Note: Spot instances can provide up to 70% cost savings compared to On-Demand pricing.

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
