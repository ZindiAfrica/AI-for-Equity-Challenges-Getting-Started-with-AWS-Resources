# SageMaker Instance Pricing

All prices are in USD per hour for the US East (Ohio) region.

## General Purpose Instances (M5)

| Instance Type    | vCPUs | Memory (GiB) | On-Demand/Hour | Spot/Hour |
|-----------------|-------|--------------|----------------|-----------|
| ml.m5.large     | 2     | 8           | $0.115         | $0.035    |
| ml.m5.xlarge    | 4     | 16          | $0.23          | $0.069    |
| ml.m5.2xlarge   | 8     | 32          | $0.46          | $0.138    |
| ml.m5.4xlarge   | 16    | 64          | $0.92          | $0.276    |

## Memory Optimized Instances (R5)

| Instance Type    | vCPUs | Memory (GiB) | On-Demand/Hour | Spot/Hour |
|-----------------|-------|--------------|----------------|-----------|
| ml.r5.2xlarge   | 8     | 64          | $0.60          | $0.18     |
| ml.r5.4xlarge   | 16    | 128         | $1.20          | $0.36     |
| ml.r5.8xlarge   | 32    | 256         | $2.40          | $0.72     |

## GPU Instances (G4DN)

| Instance Type     | vCPUs | Memory (GiB) | GPUs | GPU Memory | On-Demand/Hour | Spot/Hour |
|------------------|-------|--------------|------|------------|----------------|-----------|
| ml.g4dn.4xlarge  | 16    | 64          | 1    | 16 GB      | $1.43          | $0.429    |
| ml.g4dn.8xlarge  | 32    | 128         | 1    | 16 GB      | $2.72          | $0.816    |
| ml.g4dn.12xlarge | 48    | 192         | 4    | 64 GB      | $4.89          | $1.467    |

Note: Additional instance types may be requested but approval will be at the organizers' discretion based on availability and requirements. Contact the competition organizers if you need access to other instance types for your specific use case.

Note: Spot instances typically offer 50-70% discount from On-Demand pricing. Actual Spot prices vary based on availability and demand.
