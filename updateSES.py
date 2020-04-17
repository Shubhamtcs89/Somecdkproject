import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    
    # TODO implement
    CHARSET = "UTF-8"
    RECIPIENT= "Shubhamtcs89@gmail.com"
    SENDER= "Shubhamtcs89@gmail.com"
    client = boto3.client('ses',region_name="eu-west-1")
    try:
        response = client.send_email(
           Destination={
               'ToAddresses': [
                   RECIPIENT,
               ],
           },
           Message={
               'Body': {
                   'Html': {
                       'Charset': CHARSET,
                       'Data': "first mail from lambda through ses",
                   },
                   'Text': {
                       'Charset': CHARSET,
                       'Data': 'keep it up',
                   },
               },
               'Subject': {
                   'Charset': CHARSET,
                   'Data': 'lambda ses testing',
               },
           },
           Source=SENDER,
           # If you are not using a configuration set, comment or delete the
           # following line
        )      
     return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
        }
