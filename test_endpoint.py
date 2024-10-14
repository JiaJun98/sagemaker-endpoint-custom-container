#!/usr/bin/env python
# coding: utf-8

# ## Download test data

# In[ ]:


import boto3
import json

#https://xgboost.readthedocs.io/en/stable/get_started.html
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def provisioned_serveless():
    sagemaker_runtime = boto3.client('sagemaker-runtime')

    # Read data
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data['data'], data['target'], test_size=.2)

    payload = {"features": X_test.tolist()}
    payload = json.dumps(payload)

    # ## Invoke endpoint - provisioned
    # The realtime and serverless endpoints are invoked with the same API. Just change the endpoint name to the one you want to use

    # In[ ]:


    ENDPOINT_NAME = 'iris-classifier-endpoint'

    # In[ ]:


    #%%time
    # Invoke SageMaker endpoint
    res = sagemaker_runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME, 
        ContentType='application/json', 
        Body=payload 
    )
    res = res['Body'].read().decode()

    parsed = json.loads(res)
    print(parsed['predictions'])

if __name__ == "__main__":
    provisioned_serveless()


# ## Invoke endpoint - Async
# To use the async endpoint, we first upload the data to S3 and then invoke the endpoint with that s3 uri

# In[ ]:

###################### ASYNC Example ####################################################

# ASYNC_ENDPOINT_NAME = 'MY ASYNC ENDPOINT NAME'
# BUCKET = 'mlbucket13' # Replace with your own bucket name
# KEY = 'iris/payload.json' # Replace with your own key

# # In[ ]:


# s3 = boto3.client('s3')
# s3_uri = f's3://{BUCKET}/{KEY}'

# try:
#     s3.put_object(
#         Body=payload,
#         Bucket=BUCKET,
#         Key=KEY
#     )
#     print(f'Uploaded payload to {s3_uri}')
# except Exception as e:
#     print(e)


# # In[ ]:


# # Invoke async SageMaker endpoint
# async_response = sagemaker_runtime.invoke_endpoint_async(
#         EndpointName=ASYNC_ENDPOINT_NAME, 
#         InputLocation=s3_uri,
#         InvocationTimeoutSeconds=3600,
#         ContentType='application/json',
#         )

# # In[ ]:


# # Fetch and parse async inference result from S3
# from urllib.parse import urlparse

# output_s3_uri = async_response['OutputLocation']

# # Parse the S3 URI to extract bucket name and object key
# parsed_uri = urlparse(output_s3_uri)
# bucket_name = parsed_uri.netloc
# object_key = parsed_uri.path.lstrip('/')

# # Read the object directly into memory
# response = s3.get_object(Bucket=bucket_name, Key=object_key)
# data = response['Body'].read().decode()
# data = json.loads(data)
# print(data)

# # In[ ]:



