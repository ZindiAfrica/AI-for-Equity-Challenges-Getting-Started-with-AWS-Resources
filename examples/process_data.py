import argparse
import boto3
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from get_username import get_bucket_name, get_team_tag

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-path', type=str)
    parser.add_argument('--output-path', type=str)
    parser.add_argument('--use-gpu', type=str, default='false')
    args = parser.parse_args()
    
    # Use default paths based on username if not specified
    if not args.input_path or not args.output_path:
        bucket = get_bucket_name()
        args.input_path = args.input_path or f's3://{bucket}/raw/data.csv'
        args.output_path = args.output_path or f's3://{bucket}/processed/data.csv'
    
    return args

def preprocess_data(df):
    """Preprocess the input dataframe"""
    # Normalize numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # Handle categorical columns
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = pd.Categorical(df[col]).codes
        
    return df

def main():
    args = parse_args()
    
    # Read input data
    df = pd.read_csv(args.input_path)
    
    # Apply preprocessing
    processed_df = preprocess_data(df)
    
    # Save results
    processed_df.to_csv(args.output_path, index=False)

if __name__ == "__main__":
    main()
