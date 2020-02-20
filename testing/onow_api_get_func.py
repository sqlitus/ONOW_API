# onow api call get function

'''
call table, filter, pull data, export
'''

import requests
import pandas as pd
import os
import config
import definitions
import functions
import logging
from datetime import datetime


def onow_get(rowlimit=10000, offset=0, user=config.sandbox['user'], pwd=config.sandbox['pwd'],
             instance='https://wfmsandbox.service-now.com/api/now/table/',
             table='incident',
             query="priorityIN2,3,4^sys_created_on>=javascript:gs.dateGenerate('2020-01-01','00:00:00')",
             fields='number,assignment_group,problem_id,location,short_description,sys_created_on'
             ):

    benchmark = functions.Benchmarking()

    rowlimit = str(rowlimit)
    offset = str(offset)
    api_calls = 1
    sysparm_query = "&sysparm_query" + query
    sysparm_fields = "&sysparm_fields=" + fields

    sysparm_display_value = "&sysparm_display_value=" + "all"
    url = f'{instance}{table}?sysparm_limit={rowlimit}&sysparm_offset={offset}' + \
          sysparm_query + \
          sysparm_fields + \
          sysparm_display_value

    # Call
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers)

    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    else:
        print('Response successful')
        benchmark.elapsed()

    print('BEGINNING OF JSON FILE:', response.text[:80], 'END OF JSON FILE:', response.text[-200:], sep='\n')
    data = response.json()

    df = pd.DataFrame.from_dict(pd.json_normalize(data["result"]), orient='columns')
    output_msg = f'ROW LIMIT: {rowlimit}. COLUMNS QUERIED: {len(sysparm_fields.split(","))}. ' \
                 f'ROWS RETURNED: {df.shape[0]}. COLUMNS RETURNED: {df.shape[1]} ' \
                 f'MISSING: {int(rowlimit)-df.shape[0]} rows. {len(sysparm_fields.split(","))-df.shape[1]} columns.'
    print(output_msg)

    # log
    log_api_call_sandbox = 'log_api_call_sandbox.log'
    logging.basicConfig(filename=log_api_call_sandbox, level=logging.DEBUG)
    logging.debug(f'Call at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    logging.debug(output_msg + f'\nsysparm_query = {sysparm_query}' + f'\nsysparm_fields = {sysparm_fields}\n')

    # Save data to CSV in relative path
    output_incident = os.path.abspath(os.path.join(definitions.ROOT_DIR, f'.\\test data\\onow-api-data_incident_sysparm_limit{rowlimit}_offset{offset}_calls{api_calls}_rows{df.shape[0]}_cols{df.shape[1]}'
                                    f'_runtime{benchmark.elapsed_total}_time{datetime.now().strftime("%H%M%S")}.csv'))
    df.to_csv(output_incident, index=False)
    benchmark.elapsed(f'FINISHED EXPORT TO {output_incident}', end='yes')


print('loaded function:', 'onow_get')