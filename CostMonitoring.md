# Cost Monitoring and Budget Management

## Important Requirements

1. **Region**: All resources MUST be in **US East (Ohio) / us-east-2**
2. **Resource Tagging**: Every resource MUST be tagged with:
   ```
   team = <your-username>
   ```
   See [Resource Tagging Requirements](./TaggingRequirements.md) for details.

## Accessing the Cost Dashboard

1. In the AWS Management Console (us-east-2 region), navigate to CloudWatch
2. Click on "Dashboards" in the left navigation
3. Select the dashboard named "team-<your-username>-costs"
4. The dashboard shows:
   - Service costs breakdown (SageMaker)
   - Total accumulated costs
   - Resource utilization (CPU, Memory, GPU)
   - Active resource count (instances, jobs)

## Budget Alerts

### Configuring Alerts
To configure budget alerts and email notifications:
1. Navigate to the AWS Budgets console.
2. Create a new budget or select an existing one.
3. Set alert thresholds (e.g., 80% and 100% of the budget).
4. Add email recipients for notifications.

You can check your remaining AWS credits at any time by visiting:
`https://us-east-1.console.aws.amazon.com/billing/home#/budgets/details?name=team-comp-<YOUR-USERNAME>-budget`
(Replace <YOUR-USERNAME> with your assigned username)

You will receive email notifications when:
- Your usage reaches 80% ($320) of the $400 budget
- Your usage reaches 100% ($400) of the budget

When the budget is exceeded:
- Running resources will be automatically stopped
- New resource creation will be blocked
