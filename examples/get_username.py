import boto3
import re

def get_username_from_console():
    """Get username from AWS console session"""
    sts = boto3.client('sts')
    caller_identity = sts.get_caller_identity()
    role_arn = caller_identity['Arn']
    
    # Extract username from role ARN 
    # Format: arn:aws:sts::ACCOUNT:assumed-role/SageMakerRole-team-USERNAME/Session
    match = re.search(r'SageMakerRole-team-([\w-]+)', role_arn)
    if not match:
        raise ValueError("Could not extract username from role ARN")
    return match.group(1)

def get_username_from_notebook():
    """Get username from SageMaker notebook environment"""
    import os
    
    # Try getting from environment first
    if 'SAGEMAKER_DOMAIN_USER_PROFILE' in os.environ:
        return os.environ['SAGEMAKER_DOMAIN_USER_PROFILE']
        
    # Fallback to role ARN parsing
    return get_username_from_console()

def get_bucket_name():
    """Get the user's S3 bucket name"""
    username = get_username_from_notebook()
    return f"{username}-team-bucket"

def get_team_tag():
    """Get the team tag value for resources"""
    username = get_username_from_notebook()
    return [{'Key': 'team', 'Value': username}]

# Example usage:
if __name__ == "__main__":
    # Get username
    username = get_username_from_notebook()
    print(f"Username: {username}")
    
    # Get bucket name
    bucket = get_bucket_name()
    print(f"Bucket: {bucket}")
    
    # Get team tag
    tag = get_team_tag()
    print(f"Team tag: {tag}")
