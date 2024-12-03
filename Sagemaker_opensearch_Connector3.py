import json
import os
import io
from typing import List

import boto3
import json
import csv


from tqdm import tqdm

import json
import logging
from typing import List, Optional

import boto3
import numpy as np

from tqdm import tqdm

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# grab environment variables

#runtime = boto3.client('runtime.sagemaker')
session = boto3.Session(
aws_access_key_id=
aws_secret_access_key=
aws_session_token=

import boto3
import requests
from requests_aws4auth import AWS4Auth

host = 'https://vpc-ks-opensearch-dev-es-gudxvizp6v6ehrbesax2uzr7gq.us-west-2.es.amazonaws.com/'
region = 'us-west-2'
service = 'es'

credentials = session.get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)


path = '/_plugins/_ml/connectors/_create'
url = host + path

payload = {
  "name": "Sagemaker embedding model connector",
  "description": "Connector for my Sagemaker embedding model",
  "version": "1.0",
  "protocol": "aws_sigv4",
  "credential": {
    "roleArn": "arn:aws:iam::851725399072:role/invoke_sagemaker_model_role"
  },
  "parameters": {
    "region": "us-west-2",
    "service_name": "sagemaker"
  },
  "actions": [
    {
      "action_type": "predict",
      "method": "POST",
      "headers": {
        "content-type": "application/json"
      },
      "url": "https://runtime.sagemaker.us-west-2.amazonaws.com/endpoints/nomic-embed/invocations",
      "request_body": "{ \"texts\":\"${parameters.inputText}\"}",
      "pre_process_function": "\nStringBuilder builder = new StringBuilder();\n    builder.append(\"\\\"\");\n    String first = params.text_docs[0];\n    builder.append(first);\n    builder.append(\"\\\"\");\n    def parameters = \"{\" +\"\\\"inputText\\\":\" + builder + \"}\";\n    return  \"{\" +\"\\\"parameters\\\":\" + parameters + \"}\";",
      "post_process_function": "\n      def name = \"sentence_embedding\";\n      def dataType = \"FLOAT32\";\n      if (params.embeddings[0] == null || params.embeddings[0].length == 0) {\n        return params.message;\n      }\n      def shape = [params.embeddings[0].length];\n      def json = \"{\" +\n                 \"\\\"name\\\":\\\"\" + params.model + \"\\\",\" +\n                 \"\\\"data_type\\\":\\\"\" + dataType + \"\\\",\" +\n                 \"\\\"shape\\\":\" + shape + \",\" +\n                 \"\\\"data\\\":\" + params.embeddings[0] +\n                 \"}\";\n      return json;\n    ",
          }
        ]
}

headers = {"Content-Type": "application/json"}

r = requests.post(url, auth=awsauth, json=payload, headers=headers)
print(r.status_code)
print(r.text)





####
import jsonimport osimport iofrom typing import Listimport boto3import jsonimport csvfrom tqdm import tqdmimport jsonimport loggingfrom typing import List, Optionalimport boto3import numpy as npfrom tqdm import tqdmlogger = logging.getLogger(__name__)logger.setLevel(logging.INFO)# grab environment variables#runtime = boto3.client('runtime.sagemaker')session = boto3.Session(aws_access_key_id="ASA4MTWKGQQA666YDEL",aws_secret_access_key="vGbjlarQq9gtj0Z8QhOH3P8BdURzzbekNM1wyfl",aws_session_token="IQoJb3JpZ2luX2VjEJ//////////wEaCXVzLXdlc3QtMiJIMEYCIQCwpBzoPpYOVz5bkTGN8HKDeTpoYz3R4R//7SwsYXL/pAIhALPSuSkPLisyXfV+b/yI75b+PeYlOqHF1MoAasEzmJ0JKp4CCEgQABoMODUxNzI1Mzk5MDcyIgz4qHcipSKxzFsJiN4q+wGYhFZ9x52Nl4gI3fZABKoYrY43zxeCvyS2KpajpYuDg3bW9r+7iAxVXgd+9CW6VilpM+3h+Tkgd4vgwl9l/LBhJcYvCi+1F8Ud0SGvPtKh4MgUgzkOSfGel6YUE4cjJOKqvmyivlP8ZczGKbwiiAD3Yf/jVTUzubcCI/u9Qg5dUviAbanYkybfIkFh6rH0vIhuVP8lb4DYlpnUMJd7BszeOJDNtwpLOEzsFQx5n9p9hvsERhVVqIJA9v9SaiVhL9Jp55P5zl5/1qTovNGDtdv3m1RG6vofYyZGUZwfBC+UqQsUEM+HZe6v/Q06BPwOSR/R+7a0DltEoCkyKTDW45y6BjqcAX8hf76GwbpAQvyjrV98m/8GrP0xh5Pse94pM9/4aFaHHRWuE/EE33M8L9tr5TucuhtvDFbWKkjcs1clrSMDg0WmwbCci72V87l0bO5mEn8DUQTa7AMobD3EKTbzc4eBvU9XEiAoKGCBM8cb5o/pT8SDvPmAMyE38uyvRtPSIWJ9xdgKdoXGMu3c0uFUuK6Z/6OL4SRDO76FInbqaA==")import boto3import requestsfrom requests_aws4auth import AWS4Authhost = 'https://vpc-ks-opensearch-dev-es-gudxvizp6v6ehrbesax2uzr7gq.us-west-2.es.amazonaws.com/'region = 'us-west-2'service = 'es'credentials = session.get_credentials()awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)path = '/_plugins/_ml/connectors/_create'url = host + pathpayload = {  "name": "Sagemaker embedding model connector",  "description": "Connector for my Sagemaker embedding model",  "version": "1.0",  "protocol": "aws_sigv4",  "credential": {    "roleArn": "arn:aws:iam::851725399072:role/invoke_sagemaker_model_role"  },  "parameters": {    "region": "us-west-2",    "service_name": "sagemaker"  },  "actions": [    {      "action_type": "predict",      "method": "POST",      "headers": {        "content-type": "application/json"      },      "url": "https://runtime.sagemaker.us-west-2.amazonaws.com/endpoints/nomic-embed/invocations",      "request_body": "{ \"texts\":\"${parameters.inputText}\"}",      "pre_process_function": "\nStringBuilder builder = new StringBuilder();\n    builder.append(\"\\\"\");\n    String first = params.text_docs[0];\n    builder.append(first);\n    builder.append(\"\\\"\");\n    def parameters = \"{\" +\"\\\"inputText\\\":\" + builder + \"}\";\n    return  \"{\" +\"\\\"parameters\\\":\" + parameters + \"}\";",      "post_process_function": "\n      def name = \"sentence_embedding\";\n      def dataType = \"FLOAT32\";\n      if (params.embeddings[0] == null || params.embeddings[0].length == 0) {\n        return params.message;\n      }\n      def shape = [params.embeddings[0].length];\n      def json = \"{\" +\n                 \"\\\"name\\\":\\\"\" + params.model + \"\\\",\" +\n                 \"\\\"data_type\\\":\\\"\" + dataType + \"\\\",\" +\n                 \"\\\"shape\\\":\" + shape + \",\" +\n                 \"\\\"data\\\":\" + params.embeddings[0] +\n                 \"}\";\n      return json;\n    ",          }        ]}headers = {"Content-Type": "application/json"}r = requests.post(url, auth=awsauth, json=payload, headers=headers)print(r.status_code)print(r.text)