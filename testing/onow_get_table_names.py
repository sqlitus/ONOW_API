# Quick function to get all tables in environment

'''
note:
    table: sys_db_object
    column: label = human display name
    column: name = system object name

reference:
    https://community.servicenow.com/community?id=community_question&sys_id=5820cf21db98dbc01dcaf3231f961959
'''


import requests
import pandas as pd
import os
import config
import definitions
import functions
from datetime import datetime


def onow_get_table_names(instance='https://wfmsandbox.service-now.com/api/now/table/'):

    benchmark = functions.Benchmarking()

    # def get_table_list
    p_table = 'sys_db_object'
    sysparm_query = "&sysparm_query=" + "nameNOT LIKE00"
    sysparm_fields = "&sysparm_fields=" + "name,label"  # sys_name
    # sysparm_display_value = "&sysparm_display_value=" + "all"
    url = f'{instance}{p_table}?{sysparm_query}{sysparm_fields}'

    user = config.sandbox['user']
    pwd = config.sandbox['pwd']
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers)

    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    else:
        print('Response successful')
        benchmark.elapsed()

    data = response.json()  # print(data)
    onow_tables = pd.DataFrame.from_dict(pd.json_normalize(data["result"]), orient='columns')

    # optional: file output code
    '''
    output = os.path.abspath(os.path.join(definitions.ROOT_DIR, f'.\\test data\\onowfunc_rows{onow_tables.shape[0]}_cols{onow_tables.shape[1]}'
                                    f'_runtime{benchmark.elapsed_total}_time{datetime.now().strftime("%H%M%S")}.csv'))
    onow_tables.to_csv(output, index=False)
    benchmark.elapsed(f'FINISHED EXPORT TO {output}', end='yes')
    '''
    benchmark.elapsed(f'tables retreived.', end='yes')

    return onow_tables


# usage:
# df_tables = onow_get_table_names()  # creates df
# df_tables  # prints df
# df_tables['label'].tolist()  # prints list
# df_tables['label'][df_tables['label'].str.contains('Mob')]  # literal
# df_tables['label'][df_tables['label'].str.contains('(?i)mob', regex=True)]  # regex

