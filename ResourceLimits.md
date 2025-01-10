# AWS Resource Limits

The following limits apply to all competition participants:

## Compute Resources
- Maximum of 5 concurrent notebook instances
- Maximum of 20 vCPUs across all resources
- Instance types limited to:

### General Purpose (M5)
  - ml.m5.large ($0.115/hour on-demand, $0.035/hr spot)
    - 2 vCPU, 8 GiB memory
  - ml.m5.xlarge ($0.23/hour on-demand, $0.069/hr spot)
    - 4 vCPU, 16 GiB memory
  - ml.m5.2xlarge ($0.46/hour on-demand, $0.138/hr spot)
    - 8 vCPU, 32 GiB memory
  - ml.m5.4xlarge ($0.92/hour on-demand, $0.276/hr spot)
    - 16 vCPU, 64 GiB memory

### Memory Optimized (R5)
  - ml.r5.2xlarge ($0.60/hour on-demand, $0.18/hr spot)
    - 8 vCPU, 64 GiB memory
  - ml.r5.4xlarge ($1.20/hour on-demand, $0.36/hr spot)
    - 16 vCPU, 128 GiB memory
  - ml.r5.8xlarge ($2.40/hour on-demand, $0.72/hr spot)
    - 32 vCPU, 256 GiB memory

### GPU Instances (G4DN)
  - ml.g4dn.4xlarge ($1.43/hour on-demand, $0.429/hr spot)
    - 16 vCPU, 64 GiB memory, 1 NVIDIA T4 GPU
  - ml.g4dn.8xlarge ($2.72/hour on-demand, $0.816/hr spot)
    - 32 vCPU, 128 GiB memory, 1 NVIDIA T4 GPU
  - ml.g4dn.12xlarge ($4.89/hour on-demand, $1.467/hr spot)
    - 48 vCPU, 192 GiB memory, 4 NVIDIA T4 GPUs

Note: Additional instance types may be requested but approval will be at the organizers' discretion based on availability and requirements.

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
