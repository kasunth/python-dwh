#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import boto3
import json
import datetime
# from pip._internal import main
# # install latest version of boto3
# main(['install', '-I', '-q', 'boto3', '--target', '/tmp/', '--no-cache-dir', '--disable-pip-version-check'])
# sys.path.insert(0,'/tmp/')
# import boto3

# initialize redshift-data client in boto3
redshift_client = boto3.client('redshift-data')

def call_data_api(redshift_client, redshift_database, redshift_user, redshift_cluster_id, sql_statement, with_event=True):
    # execute the input SQL statement
    api_response = redshift_client.execute_statement(Database=redshift_database, WorkgroupName=redshift_cluster_id,Sql=sql_statement)
                                                    
    # api_response = redshift_client.execute_statement(Database=redshift_database, DbUser=redshift_user
    #                                                 ,Sql=sql_statement, workgroup-name=redshift_cluster_id, 
    #                                                 SecretArn="arn:aws:secretsmanager:eu-north-1:846996571657:secret:sandclinicsecret-xbJZ8T",
    #                                                 WithEvent=True
    #                                                 )
    
    # return the query_id
    query_id = api_response["Id"]
    return query_id

def check_data_api_status(redshift_client, query_id):
    desc = redshift_client.describe_statement(Id=query_id)
    status = desc["Status"]

    if status == "FAILED":
        raise Exception('SQL query failed:' + query_id + ": " + desc["Error"])
    return status.strip('"')

def get_api_results(redshift_client, query_id):
    response = redshift_client.get_statement_result(Id=query_id)
    return response

def lambda_handler(event, context):
    redshift_cluster_id = os.environ['redshift_cluster_id']
    redshift_database = os.environ['redshift_database']
    redshift_user = os.environ['redshift_user']
   
    action = event['queryStringParameters'].get('action')
    try:
        if action == "execute_report":
            email = event['queryStringParameters'].get('email')
            # sql report query to be submitted
            sql_statement = "select O.* from dev.public.o2saturation O where O.email = '"+ email +"' "
            api_response = call_data_api(redshift_client, redshift_database, redshift_user, redshift_cluster_id, sql_statement)
            return_status = 200
            return_body = json.dumps(api_response)

        elif action == "check_report_status":            
            # query_id to input for action check_report_status
            query_id = event['queryStringParameters'].get('query_id')            
            # check status of a previously executed query
            api_response = check_data_api_status(redshift_client, query_id)
            return_status = 200
            return_body = json.dumps(api_response)

        elif action == "get_report_results":
            # query_id to input for action get_report_results
            query_id = event['queryStringParameters'].get('query_id')
            # get results of a previously executed query
            api_response = get_api_results(redshift_client, query_id)
            return_status = 200
            return_body = json.dumps(api_response)

            # total number of rows
            nrows=api_response["TotalNumRows"]
            # number of columns
            ncols=len(api_response["ColumnMetadata"])
            print("Number of rows: %d , columns: %d" % (nrows, ncols) )

            for record in api_response["Records"]:
                print (record)
        else:
            return_status = 500
            return_body = "Invalid Action: " + action
        return_headers = {
                        "Access-Control-Allow-Headers" : "Content-Type",
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Methods": "GET"}
        return {'statusCode' : return_status,'headers':return_headers,'body' : return_body}
    except NameError as error:
        raise NameError(error)
    except Exception as exception:
        error_message = "Encountered exeption on:" + action + ":" + str(exception)
        raise Exception(error_message)
