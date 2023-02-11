#!/bin/bash

# Read the access key and secret access key from the text file
IFS=', ' read -r -a keys < "aws-access.txt"

echo "Adding AWS access key: ${keys[0]}"
echo "Adding AWS secret access key: ${keys[1]}"
echo "Adding AWS region: ${keys[2]}"


# Set the AWS CLI configuration
aws configure set aws_access_key_id "${keys[0]}"
aws configure set aws_secret_access_key "${keys[1]}"

# Optional: Set the default region
aws configure set default.region "${keys[2]}"
