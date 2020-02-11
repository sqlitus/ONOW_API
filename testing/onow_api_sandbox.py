#!/usr/bin/python3

# OrchardNow Sandbox API data pull
'''
Purpose:
test OrchardNow [sandbox] API functionality
Retreive all data from table
Access given by HS

Created:
12/19/2019

Updates:
get request times out inconsistently. 10k row limit

Reference:
https://docs.servicenow.com/bundle/madrid-application-development/page/integrate/inbound-rest/concept/c_RESTAPIExplorer.html

Note:
data contained in denormalized dict value within root dict -- converted to pd dataframe
noticing many values are ENUM IDs - not human readable -- dot-walk for names.
using v1 tables  - need to test w/ latest -- latest works, declare explicit last version for vc

'''

#Need to install requests package for python
import requests
import pandas as pd
from pandas.io.json import json_normalize
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
sysparm_fields = "&sysparm_fields=" + "promoted_by,u_incident_owner,parent,u_vendor_name,caused_by,watch_list,upon_reject,sys_updated_on,u_reported_by_manager,x_lomei_logmein_re_logmein_session_counter,approval_history,skills,number,proposed_by,lessons_learned,x_pd_integration_incident,state,sys_created_by,knowledge,order,u_business_function,u_assigned_timestamp,cmdb_ci,delivery_plan,u_application_classification,u_caller_number,u_client_reference_number,impact,u_requested_for,active,u_created_analyst_s_assignment_group,work_notes_list,priority,sys_domain_path,x_lomei_logmein_re_logmein_session_id,business_duration,group_list,approval_set,major_incident_state,u_resolved_on_first_call_eligible,x_lomei_logmein_re_logmein_closing_time,short_description,correlation_display,delivery_task,work_start,trigger_rule,additional_assignee_list,u_limited_visibility,notify,sys_class_name,closed_by,follow_up,parent_incident,u_incident_owner_group,reopened_by,u_mim_details,reassignment_count,x_pd_integration_incident_key,assigned_to,sla_due,comments_and_work_notes,u_assigned_time_elapsed,u_first_assignment_group,u_amazon_go_region,u_group_change_counter,escalation,upon_approval,correlation_id,timeline,made_sla,promoted_on,u_major_incident,child_incidents,hold_reason,resolved_by,sys_updated_by,u_resolved_on_first_call,user_input,sys_created_on,u_msp_touched,proposed_on,actions_taken,x_pd_integration_notes_ids,calendar_stc,closed_at,u_vendor_reference_number,x_86994_opsgenie_alert_alias,business_service,business_impact,rfc,time_worked,expected_start,opened_at,u_reported_by_name,x_86994_opsgenie_opsgenie_alert_id,work_end,reopened_time,resolved_at,x_lomei_logmein_re_logmein_pickup_time,subcategory,work_notes,u_unknown_name,close_code,u_incident_user_reference,x_lomei_logmein_re_logmein_work_time,business_stc,cause,description,calendar_duration,close_notes,u_manila_touched,sys_id,contact_type,incident_state,urgency,problem_id,activity_due,severity,overview,comments,approval,due_date,sys_mod_count,reopen_count,sys_tags,u_ticket_complexity,u_amazon_go_location,category,u_what_is_impacted.link,u_what_is_impacted.value,opened_by.link,opened_by.value,sys_domain.link,sys_domain.value,caller_id.link,caller_id.value,assignment_group.link,assignment_group.value,company.link,company.value,u_affected_user.link,u_affected_user.value,location.link,location.value,assignment_group.name,assignment_group.value,u_affected_user.name"
url = f'https://wfmsandbox.service-now.com/api/now/table/incident?sysparm_limit={nrows}&sysparm_offset={offset}' + \
      sysparm_query + \
      sysparm_fields

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
df = pd.DataFrame.from_dict(json_normalize(data["result"]), orient='columns')
output_msg = f'RECORD LIMIT: {record_limit}. DATA RETURNED: {df.shape[0]}. MISSING: {int(record_limit)-df.shape[0]} rows. COLUMNS: {df.shape[1]}'
print(output_msg)

# log
log_api_call_sandbox = 'log_api_call_sandbox.log'
logging.basicConfig(filename=log_api_call_sandbox, level=logging.DEBUG)
logging.debug(f'Call at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
logging.debug(output_msg + f'\nsysparm_query = {sysparm_query}' + f'\nsysparm_fields = {sysparm_fields}\n')

# Save data to CSV in relative path
output_incident = os.path.abspath(os.path.join(definitions.ROOT_DIR, f'.\\test data\\onow-api-data_incident_sysparm_limit{record_limit}_offset{offset}_calls{api_calls}_rows{df.shape[0]}_cols{df.shape[1]}'
                                f'_runtime{benchmark.elapsed_total}.csv'))
df.to_csv(output_incident, index=False)
benchmark.elapsed(f'FINISHED EXPORT TO {output_incident}', end='yes')
