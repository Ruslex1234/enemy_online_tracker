import json
import boto3
import requests

def lambda_handler(event, context):
    # Your GitHub personal access token
    token = 'YOUR_GITHUB_TOKEN'
    # The repository to trigger the workflow in
    repo = 'your_username/your_repo_name'
    # The name of your workflow file
    workflow_file = 'external-trigger.yml'
    
    url = f'https://api.github.com/repos/{repo}/actions/workflows/{workflow_file}/dispatches'
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Example payload - you can adjust this as needed
    data = {
        'ref': 'main', # or any other branch or tag
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Workflow triggered')
    }
