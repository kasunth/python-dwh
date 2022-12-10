# Set up logging
import boto3
import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Import Boto 3 for AWS Glue
client = boto3.client('glue')

# Variables for the job:
glueJobName = "synchheartrate"

# Define Lambda function


def lambda_handler(event, context):
    try:
        logger.info('## TRIGGERED BY EVENT: ')
        logger.info(event)
        # logger.info(event['body'])
        response = client.start_job_run(JobName=glueJobName)
        logger.info('## STARTED GLUE JOB: ' + glueJobName)
        logger.info('## GLUE JOB RUN ID: ' + response['JobRunId'])
        return response
    except:
        return false
