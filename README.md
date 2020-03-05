# ONOW_API

Purpose: Reference for establishing ONOW connection to SNOW API.

### Resources
- [Getting Started Guide](https://docs.servicenow.com/bundle/madrid-application-development/page/integrate/inbound-rest/concept/c_GettingStartedWithREST.html#c_GettingStartedWithREST)
- [API Call Parameters](https://developer.servicenow.com/app.do#!/rest_api_doc?v=madrid&id=r_TableAPI-GET)
- [Table API FAQs](https://hi.service-now.com/kb_view.do?sysparm_article=KB0534905) 
- [existing python2/snow package](https://community.servicenow.com/community?id=community_question&sys_id=63864b25db1cdbc01dcaf3231f961945)
- [developer acct walkthrough](http://beginnersforum.net/blog/2018/10/16/update-service-now-incident-using-python/)
- Also: links provided by HS. 
-- [1. api](https://docs.servicenow.com/bundle/madrid-application-development/page/integrate/inbound-rest/task/explore-rest-api-for-table.html). 
-- [2. odbc](https://docs.servicenow.com/bundle/newyork-application-development/page/integrate/odbc-driver/concept/c_ODBCDriver.html).


### Environment
Python 3.8+. Windows 10. Pycharm. SNOW Madrid.

### Notes
Testing in sandbox initially. Will need access to prod.
Current Table API Version: 2.
Backend timestamps are in UTC. Display values will show central (queried from central).
param `sysparm_display_value=all` required for returning both field IDs & human-readable display values.

### API Setup Workflow
1. Get api access to ONOW for an account (ask ONOW admins).
2. In ONOW ITIL view, navigate to Rest API Explorer.
3. Run a sample GET request on the [incident] table, following directions in the [getting started guide](https://docs.servicenow.com/bundle/madrid-application-development/page/integrate/inbound-rest/concept/c_GettingStartedWithREST.html#c_GettingStartedWithREST).
4. Select code language on page below (python). Copy code, paste into IDE (e.g. PyCharm).
5. In Python environment, install necessary packages (requests, pandas). 
6. In code, remove/change rowlimit params `sysparm_limit` to larger number or remove. (default sample code limits output to <=10 records.
7. ServiceNow Admins must change properties for user account REST API settings to allow larger data pulls, e.g. increase query timeout length. Default time limit for query execution is too short.
8. For query parameters `sysparm_query`, go to list view, right click on filters, select "copy query" for correct filter syntax. Reference [API Call Parameters](https://developer.servicenow.com/app.do#!/rest_api_doc?v=madrid&id=r_TableAPI-GET) for more about input parameters.

### Issues addressed (& resolution)

1. incorrect row amt (admin, sec permission)
2. larger query timeout (admin, execution length)
3. missing columns (admin, sec permission)
4. dot-walk name fields not selected by default. Missing other dot-walk fields (link, value) when name is explicitly selected in sysparm_fields. (link and value fields cannot be explicitly added. Add root field name to select them, along with other dot-walk fields needed)
5. custom fields (user tables) do not return name values. need to find how to call these. (sysparm_display_value=all returns sys_ids values and display values. negates issue #4 and need to specify fields for names)

### Sample parameters

same thing:
(Priority 'is one of' 2,3,4 AND created on >= this year)
```
priorityIN2,3,4^sys_created_on>=javascript:gs.beginningOfThisYear()
priorityIN2,3,4^sys_created_on>=javascript:gs.dateGenerate('2020-01-01','00:00:00')
```

### Reporting Solution Timeline
Milestones:
- Q1 - Successfully connected to ONOW Sandbox REST API.
- Q1 - Validated data pulls. Resolved data discrepancy issues w/ Unisys Integrations team (needed correct permissions).

Current/ongoing:
- Exploring data structure, API parameters, performance, capabilities.

Next Steps & Estimated deadlines:
- Q2 - (current obstacle) Need REST API permissions in Prod environment to pull Prod data.
- Q2 - Need service account(s) created for ETL/reporting use.
- Q3 - Procure data storage location + host for ETL processes.
- Q3 - More testing & validating data, performance. configure api calls as necessary. 
- Q4 - Create custom fields & views for reporting.
- Q4 - (Finally) connect to data store from Tableau Server, create all manner of reports.
