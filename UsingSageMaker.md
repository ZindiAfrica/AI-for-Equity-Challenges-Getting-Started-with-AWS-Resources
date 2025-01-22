# Getting Started with SageMaker

## Quick Links

- [AWS Console Login](https://zindicomp.signin.aws.amazon.com/console)
- [SageMaker Studio](https://us-east-2.console.aws.amazon.com/sagemaker/home?region=us-east-2#/studio-landing)
- [ECR Repositories](https://us-east-2.console.aws.amazon.com/ecr/repositories?region=us-east-2)
- [CodeCommit Repositories](https://us-east-2.console.aws.amazon.com/codesuite/codecommit/repositories?region=us-east-2)

## Important Requirements

1. **Region**: All resources MUST be created in **US East (Ohio) / us-east-2**
2. **Resource Tagging**: Every resource you create MUST be tagged with:

   ```
   team = <your-username>
   ```

   See [Resource Tagging Requirements](./TaggingRequirements.md) for details.
3. **Instance Pricing**: For current pricing and instance specifications, see:
   - [Instance Pricing Guide](./aws-pricing/instance_pricing.md)
   - [Detailed Instance Data](./aws-pricing/instance_data.json)

## Quick Start: Opening SageMaker Studio

1. Go to [SageMaker in AWS Console](https://us-east-2.console.aws.amazon.com/sagemaker/home?region=us-east-2#/studio-landing)
2. Verify you're in the **US East (Ohio)** region
3. Click "Studio" in the left menu
4. Select your domain and username (they match your competition username)
5. Click "Open Studio"

That's it! You'll get a familiar Jupyter Lab interface where you can start coding.

See [AWS Access Guide](./AWSAccess.md) for help with credentials and setup.

## Source Control & Container Registry

### Source Control Options

#### Using GitHub

You can connect your SageMaker environment directly to GitHub:

1. Create a GitHub repository for your project
2. In SageMaker Studio, click the Git icon in the left sidebar
3. Choose "Clone a Repository"
4. Enter your GitHub repository URL
5. Authenticate using GitHub credentials or token

The integration allows you to:

- Clone repositories
- Commit and push changes
- Create branches
- View git history
- Manage pull requests

For more details, see [GitHub Integration Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-git-attach.html)

### Container Registry (ECR)

Each user has a private Amazon Elastic Container Registry (ECR) repository for storing Docker images:

1. Your repository is named: `<username>-workspace`
2. Access via [ECR Console](https://us-east-2.console.aws.amazon.com/ecr/repositories?region=us-east-2)
3. Full repository URL: `<account-id>.dkr.ecr.us-east-2.amazonaws.com/<username>-workspace`
4. See [ECR Paths Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg-ecr-paths/ecr-us-east-2.html) for available container images

To push images:

```bash
# Login to ECR
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-2.amazonaws.com

# Tag and push your image
docker tag my-image:latest <account-id>.dkr.ecr.us-east-2.amazonaws.com/<username>-workspace:latest
docker push <account-id>.dkr.ecr.us-east-2.amazonaws.com/<username>-workspace:latest
```

## Training Your Models

You have two main options:

1. **Simple Option: SageMaker Notebooks**

   - Just like Jupyter, but with more compute power
   - Good for development and small training runs
   - Use this when getting started

2. **Advanced Option: SageMaker Training Jobs**
   - For training on full datasets
   - Multiple instance types available
   - Automatic resource scaling
   - See [Training Models](./TrainingModels.md) for details

## Important Tips

1. Start with small data while developing
2. Monitor your costs in [Cost Dashboard](./CostMonitoring.md)
3. Check [Resource Limits](./ResourceLimits.md) before running big jobs
4. See [ML Training Guidelines](./MLTrainingCommon.md) for best practices

Need help? Check the competition forums or AWS documentation.
