# Hist log

Working notes as API connection is established.

## Table Priorities for Connections
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
- various parameters. copy query params via [list view](https://docs.servicenow.com/bundle/newyork-platform-user-interface/page/use/using-lists/concept/c_UseLists.html), breadcrumbs
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

### 2/12/2020 - continue addressing missing dot-walk fields
fields selected:

    sysparm_fields = "&sysparm_fields=" + "u_amazon_go_location,category,u_what_is_impacted.link,u_what_is_impacted.value,opened_by.link,opened_by.value,sys_domain.link,sys_domain.value,caller_id.link,caller_id.value,assignment_group.link,assignment_group.value,company.link,company.value,u_affected_user.link,u_affected_user.value,location.link,location.value,assignment_group.name,assignment_group.value,u_affected_user.name"

only 4 returned:

    u_affected_user.name	category	assignment_group.name	u_amazon_go_location

found [Table API FAQs](https://hi.service-now.com/kb_view.do?sysparm_article=KB0534905)

> answer: select base field for like & value, then field.name for display. 
> returns all 3 correctly:

    sysparm_fields = "&sysparm_fields=" + "assignment_group,assignment_group.name"

assignment_group.name | assignment_group.link	| assignment_group.value
--- | --- | ---
Retail Support	| (url with id)	| (id)
Retail Support L2 |	(url with id) |	(id)

testing now with all 177 cols seen, plus additional root names + dotwalk fields
177 cols:
    
    promoted_by,u_incident_owner,parent,u_vendor_name,caused_by,watch_list,upon_reject,sys_updated_on,u_reported_by_manager,x_lomei_logmein_re_logmein_session_counter,approval_history,skills,number,proposed_by,lessons_learned,x_pd_integration_incident,state,sys_created_by,knowledge,order,u_business_function,u_assigned_timestamp,delivery_plan,u_application_classification,u_caller_number,u_client_reference_number,impact,u_requested_for,active,u_created_analyst_s_assignment_group,work_notes_list,priority,sys_domain_path,x_lomei_logmein_re_logmein_session_id,business_duration,group_list,approval_set,major_incident_state,u_resolved_on_first_call_eligible,x_lomei_logmein_re_logmein_closing_time,short_description,correlation_display,delivery_task,work_start,trigger_rule,additional_assignee_list,u_limited_visibility,notify,sys_class_name,closed_by,follow_up,parent_incident,u_incident_owner_group,reopened_by,u_mim_details,u_what_is_impacted,reassignment_count,x_pd_integration_incident_key,sla_due,comments_and_work_notes,u_assigned_time_elapsed,u_first_assignment_group,u_amazon_go_region,u_group_change_counter,escalation,upon_approval,correlation_id,timeline,made_sla,promoted_on,u_major_incident,child_incidents,hold_reason,resolved_by,sys_updated_by,u_resolved_on_first_call,user_input,sys_created_on,u_msp_touched,proposed_on,actions_taken,x_pd_integration_notes_ids,calendar_stc,closed_at,u_vendor_reference_number,x_86994_opsgenie_alert_alias,business_impact,rfc,time_worked,expected_start,opened_at,u_reported_by_name,x_86994_opsgenie_opsgenie_alert_id,work_end,reopened_time,resolved_at,x_lomei_logmein_re_logmein_pickup_time,subcategory,work_notes,u_unknown_name,close_code,u_incident_user_reference,x_lomei_logmein_re_logmein_work_time,business_stc,cause,description,calendar_duration,close_notes,u_manila_touched,sys_id,contact_type,incident_state,urgency,problem_id,activity_due,severity,overview,comments,approval,due_date,sys_mod_count,u_affected_user,reopen_count,sys_tags,u_ticket_complexity,u_amazon_go_location,location,category,cmdb_ci.link,cmdb_ci.value,assigned_to.link,assigned_to.value,opened_by.link,opened_by.value,sys_domain.link,sys_domain.value,business_service.link,business_service.value,caller_id.link,caller_id.value,assignment_group.link,assignment_group.value,company.link,company.value,assigned_to,parent_incident.link,parent_incident.value,cmdb_ci,business_service,assignment_group,delivery_plan.link,delivery_plan.value,delivery_task.link,delivery_task.value,trigger_rule.link,trigger_rule.value,opened_by,caller_id,company,u_business_function.link,u_business_function.value,closed_by.link,closed_by.value,u_what_is_impacted.link,u_what_is_impacted.value,resolved_by.link,resolved_by.value,u_affected_user.link,u_affected_user.value,location.link,location.value,rfc.link,rfc.value,parent.link,parent.value,problem_id.link,problem_id.value
    
extra:

    assignment_group,assignment_group.name,
    x_pd_integration_incident_key,x_pd_integration_incident_key.name,
    -- priority,priority.name,priority.value,
    problem_id,problem_id.name,
    u_what_is_impacted,u_what_is_impacted.name
    
running default query, grabbing col list, removing .link + .value fields, then running, adding extra.
144 base fields:

    "promoted_by,u_incident_owner,parent,u_vendor_name,caused_by,watch_list,upon_reject,sys_updated_on,u_reported_by_manager,x_lomei_logmein_re_logmein_session_counter,approval_history,skills,number,proposed_by,lessons_learned,x_pd_integration_incident,state,sys_created_by,knowledge,order,u_business_function,u_assigned_timestamp,delivery_plan,u_application_classification,u_caller_number,u_client_reference_number,impact,u_requested_for,active,u_created_analyst_s_assignment_group,work_notes_list,priority,sys_domain_path,x_lomei_logmein_re_logmein_session_id,business_duration,group_list,approval_set,major_incident_state,u_resolved_on_first_call_eligible,x_lomei_logmein_re_logmein_closing_time,short_description,correlation_display,delivery_task,work_start,trigger_rule,additional_assignee_list,u_limited_visibility,notify,sys_class_name,closed_by,follow_up,parent_incident,u_incident_owner_group,reopened_by,u_mim_details,u_what_is_impacted,reassignment_count,x_pd_integration_incident_key,sla_due,comments_and_work_notes,u_assigned_time_elapsed,u_first_assignment_group,u_amazon_go_region,u_group_change_counter,escalation,upon_approval,correlation_id,timeline,made_sla,promoted_on,u_major_incident,child_incidents,hold_reason,resolved_by,sys_updated_by,u_resolved_on_first_call,user_input,sys_created_on,u_msp_touched,proposed_on,actions_taken,x_pd_integration_notes_ids,calendar_stc,closed_at,u_vendor_reference_number,x_86994_opsgenie_alert_alias,business_impact,rfc,time_worked,expected_start,opened_at,u_reported_by_name,x_86994_opsgenie_opsgenie_alert_id,work_end,reopened_time,resolved_at,x_lomei_logmein_re_logmein_pickup_time,subcategory,work_notes,u_unknown_name,close_code,u_incident_user_reference,x_lomei_logmein_re_logmein_work_time,business_stc,cause,description,calendar_duration,close_notes,u_manila_touched,sys_id,contact_type,incident_state,urgency,problem_id,activity_due,severity,overview,comments,approval,due_date,sys_mod_count,u_affected_user,reopen_count,sys_tags,u_ticket_complexity,u_amazon_go_location,location,category,cmdb_ci,cmdb_ci,assigned_to,assigned_to,opened_by,opened_by,sys_domain,sys_domain,business_service,business_service,caller_id,caller_id,assignment_group,assignment_group,company,company,assigned_to,parent_incident,parent_incident,cmdb_ci,business_service,assignment_group,delivery_plan,delivery_plan,delivery_task,delivery_task,trigger_rule,trigger_rule,opened_by,caller_id,company,u_business_function,u_business_function,closed_by,closed_by,u_what_is_impacted,u_what_is_impacted,resolved_by,resolved_by,u_affected_user,u_affected_user,location,location,rfc,rfc,parent,parent,problem_id,problem_id"
    
> correctly added 1 field per root+name pair
> .name or .number or whatever applies to field

Reference for display: `https://stackoverflow.com/questions/36634879/retrieving-text-state-from-servicenow-rest-api/36655809#36655809`

Solution:
sysparm_display_value "all" param returns both. likely don't need dot-walk specified fields.
test no sys_fields, display all.
> display value, value, and link returned when applicable.

 (***API GET calls working in sandbox***)

noticing cooldown between requests? (nvm, func is fine)

issue: date param from gs func w/ string not being honored `javascript:gs.dateGenerate('2020-01-01','00:00:00')`.
trying simpler func. `javascript:gs.beginningOfThisYear()`.
not working either. param typo - no "=".
`sys_created_onONLast year@javascript:gs.beginningOfLastYear()@javascript:gs.endOfLastYear()`

## work on POST (create) requests
sandbox.
[create an incident record section](https://docs.servicenow.com/bundle/madrid-application-development/page/integrate/inbound-rest/concept/c_GettingStartedWithREST.html#t_GetStartedCreateInt)
works with minimal inputs.
assignment  group - use sys_id? incorrect values ignored, not created.
few default values assigned, priority, state. 
assign w/ name works.