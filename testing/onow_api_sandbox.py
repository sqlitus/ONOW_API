#!/usr/bin/python3

# OrchardNow Sandbox API data pull
'''
Purpose:
test OrchardNow [sandbox] API functionality
Retreive all data from table
Access given by HS

Created:
12/19/2019

Note:
data contained in denormalized dict value within root dict -- converted to pd dataframe
noticing many values are ENUM IDs - not human readable -- dot-walk for names.
using current (v2) tables

'''


import requests
import pandas as pd
import os
import config
import definitions
import functions
import logging
from datetime import datetime

benchmark = functions.Benchmarking()


# def onow_api_call(nrows=1, user=config.sandbox['user'], pwd=config.sandbox['pwd']):

# Set the request parameters
nrows = 129; record_limit = str(nrows)
noffset = 0; offset = str(noffset)
api_calls = 1
sysparm_query = "&sysparm_query=priorityIN2,3,4^sys_created_on>=javascript:gs.dateGenerate('2020-01-01','00:00:00')^assignment_group.nameLIKEretail"
sysparm_fields = "&sysparm_fields=" + "assignment_group,problem_id,number,location,location.lattitude,location.longitude"
sysparm_display_value = "&sysparm_display_value=" + "all"
url = f'https://wfmsandbox.service-now.com/api/now/table/incident?sysparm_limit={nrows}&sysparm_offset={offset}' + \
      sysparm_query + \
      sysparm_fields + \
      sysparm_display_value

user = config.sandbox['user']
pwd = config.sandbox['pwd']

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()
else:
    print('Response successful')
    benchmark.elapsed()

# Decode the JSON response into a dictionary and use the data
print('BEGINNING OF JSON FILE:', response.text[:80], 'END OF JSON FILE:', response.text[-200:], sep='\n')
data = response.json()  # print(data)

# Convert JSON to Dataframe. Data contained in dictionaries within dictionary, within single value dictionary
df = pd.DataFrame.from_dict(pd.json_normalize(data["result"]), orient='columns')
output_msg = f'ROW LIMIT: {record_limit}. COLUMNS QUERIED: {len(sysparm_fields.split(","))}. ' \
             f'ROWS RETURNED: {df.shape[0]}. COLUMNS RETURNED: {df.shape[1]} ' \
             f'MISSING: {int(record_limit)-df.shape[0]} rows. {len(sysparm_fields.split(","))-df.shape[1]} columns.'
print(output_msg)

# log
log_api_call_sandbox = 'log_api_call_sandbox.log'
logging.basicConfig(filename=log_api_call_sandbox, level=logging.DEBUG)
logging.debug(f'Call at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
logging.debug(output_msg + f'\nsysparm_query = {sysparm_query}' + f'\nsysparm_fields = {sysparm_fields}\n')

# Save data to CSV in relative path
output_incident = os.path.abspath(os.path.join(definitions.ROOT_DIR, f'.\\test data\\onow-api-data_incident_sysparm_limit{record_limit}_offset{offset}_calls{api_calls}_rows{df.shape[0]}_cols{df.shape[1]}'
                                f'_runtime{benchmark.elapsed_total}_time{datetime.now().strftime("%H%M%S")}.csv'))
df.to_csv(output_incident, index=False)
benchmark.elapsed(f'FINISHED EXPORT TO {output_incident}', end='yes')
