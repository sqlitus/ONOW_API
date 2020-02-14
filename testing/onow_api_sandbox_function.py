# get Table names

'''
sys_db_object
label = display name
name = object name
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

# def get_table_list
p_table = 'sys_db_object'
sysparm_query = "&sysparm_query=" + "nameNOT LIKE00"
sysparm_fields = "&sysparm_fields=" + "name,label"  # sys_name
# sysparm_display_value = "&sysparm_display_value=" + "all"
url = f'https://wfmsandbox.service-now.com/api/now/table/{p_table}?{sysparm_query}{sysparm_fields}'

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
df = pd.DataFrame.from_dict(pd.json_normalize(data["result"]), orient='columns')
output = os.path.abspath(os.path.join(definitions.ROOT_DIR, f'.\\test data\\onowfunc_rows{df.shape[0]}_cols{df.shape[1]}'
                                f'_runtime{benchmark.elapsed_total}_time{datetime.now().strftime("%H%M%S")}.csv'))
df.to_csv(output, index=False)
benchmark.elapsed(f'FINISHED EXPORT TO {output}', end='yes')

# output list
df['label']