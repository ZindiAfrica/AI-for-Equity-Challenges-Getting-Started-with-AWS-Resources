# SageMaker Instance Pricing

All prices are in USD per hour for the US East (Ohio) region.

## General Purpose Instances (T3/T3A)

| Instance Type    | vCPUs | Memory (GiB) | On-Demand/Hour | Spot/Hour |
|-----------------|-------|--------------|----------------|-----------|
| ml.t3.medium    | 2     | 4           | $0.05          | $0.015    |
| ml.t3.large     | 2     | 8           | $0.10          | $0.03     |
| ml.t3.xlarge    | 4     | 16          | $0.20          | $0.06     |
| ml.t3a.xlarge   | 4     | 16          | $0.18          | $0.054    |
| ml.t3.2xlarge   | 8     | 32          | $0.40          | $0.12     |
| ml.t3a.2xlarge  | 8     | 32          | $0.36          | $0.108    |

## General Purpose Instances (M5)

| Instance Type    | vCPUs | Memory (GiB) | On-Demand/Hour | Spot/Hour |
|-----------------|-------|--------------|----------------|-----------|
| ml.m5.large     | 2     | 8           | $0.115         | $0.035    |
| ml.m5.xlarge    | 4     | 16          | $0.23          | $0.069    |
| ml.m5.2xlarge   | 8     | 32          | $0.46          | $0.138    |
| ml.m5.4xlarge   | 16    | 64          | $0.92          | $0.276    |

## Memory Optimized Instances (R5/R5A)

| Instance Type    | vCPUs | Memory (GiB) | On-Demand/Hour | Spot/Hour |
|-----------------|-------|--------------|----------------|-----------|
| ml.r5.large     | 2     | 16          | $0.15          | $0.045    |
| ml.r5.xlarge    | 4     | 32          | $0.30          | $0.09     |
| ml.r5.2xlarge   | 8     | 64          | $0.60          | $0.18     |
| ml.r5a.2xlarge  | 8     | 64          | $0.54          | $0.162    |
| ml.r5.4xlarge   | 16    | 128         | $1.20          | $0.36     |
| ml.r5a.4xlarge  | 16    | 128         | $1.08          | $0.324    |
| ml.r5a.8xlarge  | 32    | 256         | $2.16          | $0.648    |
| ml.r5.8xlarge   | 32    | 256         | $2.40          | $0.72     |

## GPU Instances (G4DN/G4AD)

| Instance Type     | vCPUs | Memory (GiB) | GPUs | GPU Memory | On-Demand/Hour | Spot/Hour |
|------------------|-------|--------------|------|------------|----------------|-----------|
| ml.g4dn.xlarge   | 4     | 16          | 1    | 16 GB      | $0.736         | $0.221    |
| ml.g4ad.2xlarge  | 8     | 32          | 1    | 8 GB       | $0.81          | $0.243    |
| ml.g4dn.2xlarge  | 8     | 32          | 1    | 16 GB      | $0.90          | $0.27     |
| ml.g4dn.4xlarge  | 16    | 64          | 1    | 16 GB      | $1.43          | $0.429    |
| ml.g4ad.4xlarge  | 16    | 64          | 1    | 8 GB       | $1.29          | $0.387    |
| ml.g4ad.8xlarge  | 32    | 128         | 2    | 16 GB      | $2.58          | $0.774    |
| ml.g4dn.8xlarge  | 32    | 128         | 1    | 16 GB      | $2.72          | $0.816    |
| ml.g4dn.12xlarge | 48    | 192         | 4    | 64 GB      | $4.89          | $1.467    |
| ml.g4ad.16xlarge | 64    | 256         | 4    | 32 GB      | $5.16          | $1.548    |
| ml.g4dn.16xlarge | 64    | 256         | 1    | 16 GB      | $5.43          | $1.629    |

## GPU Instances (P3)

| Instance Type    | vCPUs | Memory (GiB) | GPUs | GPU Memory | On-Demand/Hour | Spot/Hour |
|-----------------|-------|--------------|------|------------|----------------|-----------|
| ml.p3.2xlarge   | 8     | 61          | 1    | 16 GB      | $3.06          | $0.918    |
| ml.p3.8xlarge   | 32    | 244         | 4    | 64 GB      | $12.24         | $3.672    |

Note: Spot instances typically offer 50-70% discount from On-Demand pricing. Actual Spot prices vary based on availability and demand.
