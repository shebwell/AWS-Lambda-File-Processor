import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Process the file here
    print(f"Processing file: {file_key} from bucket: {bucket_name}")

    return {
        'statusCode': 200,
        'body': 'File processed successfully'
    }

