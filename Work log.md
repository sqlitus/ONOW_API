# Hist log

## Table Priorities
- incident
- prob / change
- request

## Log
### Initial links Provided by HS:
- [Explore the REST API for a table](https://docs.servicenow.com/bundle/madrid-application-development/page/integrate/inbound-rest/task/explore-rest-api-for-table.html)
- [ODBC driver](https://docs.servicenow.com/bundle/newyork-application-development/page/integrate/odbc-driver/concept/c_ODBCDriver.html)




### too many rows error?
    Transaction cancelled: maximum execution time exceeded 
    Check logs for error trace or enable glide.rest.debug property to verify REST request processing","message":"Transaction cancelled: maximum execution time exceeded"},"status":"failure"}
---

#### 2020-01. debug API. problem: < 10k row limit & not all data pulled.
https://community.servicenow.com/community?id=community_question&sys_id=f7e087a5db98dbc01dcaf3231f961913
xml: `"Record doesn't exist or ACL restricts the record retrieval"`
doesn't matter what script method.
follow up: https://community.servicenow.com/community?id=community_question&sys_id=ee160f61db1cdbc01dcaf3231f961911
altering sysparm, latest version, still isn't working.
around 4-6k rows is limit before timeout (inconsistent)
useful resource?: https://developer.servicenow.com/blog.do?p=/post/debugging-inbound-rest-calls-and-the-business-rulesacls-that-impact-those-calls/
note: query limit around ~10mb of CSV data. happens regardless of version (v1 vs default v2)
API offset tests confirm missing data are real rows somehow being ignored in call. data appends cleanly in 100 rowlimit query increments, even when rows returned are < rowlimit. results support permission/security hypothesis.
detailed case: "Table REST API returns duplicates / inconsistent data sets" https://community.servicenow.com/community?id=community_question&sys_id=bd7f8725dbdcdbc01dcaf3231f961949
	

### problem: not all data rows pull (e.g. pull 10k only returns 9,788)
	hypothesis: related to my access, and how ServiceNow internally filters out data which is not accessible via the View Domains 
	https://community.servicenow.com/community?id=community_question&sys_id=bd7f8725dbdcdbc01dcaf3231f961949
---


### 1/22/2020 - continue work. 
all permissions, so records all pulled correctly.  

    {"result": 
	[{"promoted_by": "", "u_incident_owner": "", "parent": "", "u_vendor_name": "", "caused_by": "", "watch_list": "", "upon_reject": "cancel", "sys_updated_on": "2019-07-30 07:00:03", "u_reported_by_manager": "", "x_lomei_logmein_re_logmein_session_counter": "", "approval_history": "", "skills": "", "number": "INC0000503", "proposed_by": "", "lessons_learned": "", "x_pd_integration_incident": "", "state": "6", "sys_created_by": "admin", "knowledge": "false", "order": "", "u_business_function": "", "u_assigned_timestamp": "", "cmdb_ci": {"link": "https://wfmsandbox.service-now.com/api/now/v1/table/cmdb_ci/26e44e8a0a0a0bb40095ff953f9ee520", "value": "26e44e8a0a0a0bb40095ff953f9ee520"}, "u_application_classification": "", "u_caller_number": "", "u_client_reference_number": "", "impact": "1", "u_requested_for": "", "active": "true", "u_created_analyst_s_assignment_group": "", "work_notes_list": "", "priority": "1", "sys_domain_path": "/", "x_lomei_logmein_re_logmein_session_id": "", "business_duration": "", "group_list": "", "approval_set": "", "major_incident_state": "accepted", "u_resolved_on_first_call_eligible": "false", "x_lomei_logmein_re_logmein_closing_time": "", "short_description": "SAP Materials Mgmt outage", "correlation_display": "", "work_start": "", "additional_assignee_list": "", "u_limited_visibility": "false", "notify": "1", "sys_class_name": "incident", "closed_by": "", "follow_up": "", "parent_incident": "", "u_incident_owner_group": "", "reopened_by": "", "u_mim_details": "", "u_what_is_impacted": "", "reassignment_count": "0", "x_pd_integration_incident_key": "", "assigned_to": {"link": "https://wfmsandbox.service-now.com/api/now/v1/table/sys_user/46d44a23a9fe19810012d100cca80666", "value": "46d44a23a9fe19810012d100cca80666"}, "sla_due": "", "comments_and_work_notes": "", "u_assigned_time_elapsed": "", "u_first_assignment_group": "", "u_amazon_go_region": "", "u_group_change_counter": "", "escalation": "0", "upon_approval": "proceed", "correlation_id": "", "timeline": "", "made_sla": "true", "promoted_on": "", "u_major_incident": "false", "child_incidents": "1", "hold_reason": "", "resolved_by": "", "sys_updated_by": "system", "opened_by": {"link": "https://wfmsandbox.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "u_resolved_on_first_call": "false", "user_input": "", "sys_created_on": "2017-09-15 21:39:13", "sys_domain": {"link": "https://wfmsandbox.service-now.com/api/now/v1/table/sys_user_group/global", "value": "global"}, "u_msp_touched": "false", "proposed_on": "", "actions_taken": "", "x_pd_integration_notes_ids": "", "calendar_stc": "", "closed_at": "", "u_vendor_reference_number": "", "x_86994_opsgenie_alert_alias": "", "business_service": {"link": "https://wfmsandbox.service-now.com/api/now/v1/table/cmdb_ci_service/26e44e8a0a0a0bb40095ff953f9ee520", "value": "26e44e8a0a0a0bb40095ff953f9ee520"}, "business_impact": "Multiple users affected by outage", "rfc": "", "time_worked": "", "expected_start": "", "opened_at": "2017-09-15 21:31:52", "u_reported_by_name": "", "x_86994_opsgenie_opsgenie_alert_id": "", "work_end": "", "caller_id": {"link": "https://wfmsandbox.service-now.com/api/now/v1/table/sys_user/d2826bf03710200044e0bfc8bcbe5dc9", "value": "d2826bf03710200044e0bfc8bcbe5dc9"}, "reopened_time": "", "resolved_at": "", "x_lomei_logmein_re_logmein_pickup_time": "", "subcategory": "", "work_notes": "", "u_unknown_name": "", "close_code": "Closed Per Policy", "assignment_group": {"link": "https://wfmsandbox.service-now.com/api/now/v1/table/sys_user_group/d625dccec0a8016700a222a0f7900d06", "value": "d625dccec0a8016700a222a0f7900d06"}, "u_incident_user_reference": "", "x_lomei_logmein_re_logmein_work_time": "", "business_stc": "", "cause": "", "description": "Application does not load for multiple users", "calendar_duration": "", "close_notes": "", "u_manila_touched": "false", "sys_id": "e93520aca5554300964fa3aa92874179", "contact_type": "phone", "incident_state": "2", "urgency": "1", "problem_id": "", "company": {"link": "https://wfmsandbox.service-now.com/api/now/v1/table/core_company/81fca4cbac1d55eb355b4b6db0e3c80f", "value": "81fca4cbac1d55eb355b4b6db0e3c80f"}, "activity_due": "2017-09-20 14:13:40", "severity": "3", "overview": "", "comments": "", "approval": "not requested", "due_date": "", "sys_mod_count": "62", "u_affected_user": "", "reopen_count": "0", "sys_tags": "", "u_ticket_complexity": "", "u_amazon_go_location": "", "location": "", "category": "inquiry"}]
    }
---


### api meeting w/ Devs
Problems to address:
1. query times out too quickly (e.g. 3k data pull works, 5k times out)
2. query does not pull all data (e.g. 3k rows queried, 2860 returned)
3. query returns inconsistent / lacking columns (e.g. 156, 168 columns based on pull size)

sandbox: pull more records w/o timing out.
get rest api.
rowlimit api pull - timeout value?
transaction quota? duration 298? timeout 60sec?, 60, 30, ...
quota changed from 30 to 500.
deactivated OOB rule. worked. "system restrict query - if not caller id, restrict user through request call"
both rowcount & amount issue corrected. 171 columns - all data?
glide.rest.debug message helpful.
variation - validation - deactivated. was affecting missing rows as well.

 - api qs:
	- order? appars to be created date (starts 2017)
	- inc metric data?
	- join data?
	- s team - service account. - see missing records. 3 missing columns.


3 columns missing in restricted pulls (acl...):
delivery_plan
delivery_task
trigger_rule
...bhavana + pinaki to confirm back about columns ...

Remaining roadblocks for API reporting usage:
1. API calls to join 
2. set up service account with permissions to pull all data
---


### 2/5/2020 onow api continued. joining tables, params. ----
https://community.servicenow.com/community?id=community_question&sys_id=2f3b0feddb5cdbc01dcaf3231f9619ec
- use db view? would need to make...

https://developer.servicenow.com/app.do#!/rest_api_doc?v=madrid&id=r_TableAPI-GET
- relying on join via sysparm_query in rest API.

https://community.servicenow.com/community?id=community_question&sys_id=e2790f65db5cdbc01dcaf3231f9619ed
https://docs.servicenow.com/bundle/newyork-platform-user-interface/page/use/using-lists/concept/c_UseLists.html
- various parameters. copy query params via list view, breadcrumbs
- list view & csv exports show column names
- assignment_group filters via enumID under the hood.


    assignment_group=ce0815ad6f9c8300eef579331c3ee4e6^sys_created_on>=javascript:gs.dateGenerate('2020-01-01','00:00:00')^priorityIN2,3,4
    assignment_group=ce0815ad6f9c8300eef579331c3ee4e6^sys_created_on>=javascript:gs.dateGenerate('2020-01-01','00:00:00')^priorityIN2,3,4^assignment_group.nameLIKEretail


https://community.servicenow.com/community?id=community_question&sys_id=415c3be4db03e3002e8c2183ca96195c
- solution to get group names instead of sys_id
- `&sysparm_fields=group.name`

dot walk no problem. add to sys_query
https://community.servicenow.com/community?id=community_question&sys_id=f27d6c80db412fc41cd8a345ca9619a5
- notice other dot-walk fields disappear when additional non-default field is specified.

* run code execute vs script - diff work dir *
---