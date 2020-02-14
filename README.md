# ONOW_API

Purpose: Reference for establishing ONOW connection to SNOW API.

### Resources
- [Explore the REST API for a table](https://docs.servicenow.com/bundle/madrid-application-development/page/integrate/inbound-rest/task/explore-rest-api-for-table.html)
- [ODBC driver](https://docs.servicenow.com/bundle/newyork-application-development/page/integrate/odbc-driver/concept/c_ODBCDriver.html)
- [Table API FAQs](https://hi.service-now.com/kb_view.do?sysparm_article=KB0534905) 
- [existing python/snow package](https://community.servicenow.com/community?id=community_question&sys_id=63864b25db1cdbc01dcaf3231f961945)

### Environment
Pycharm. Python 3.8+. Windows 10.

### Notes
Testing in sandbox initially. Will need access to prod.
Current Table API Version: 2.
Times are in UTC. Display values show central (queried from central).
"sysparm_display_value=all" required for returning both IDS & human-readable values.

### Issues addressed (& resolution)
1. incorrect row amt (admin, sec permission)
2. larger query timeout (admin, execution length)
3. missing columns (admin, sec permission)
4. dot-walk name fields not selected by default. Missing other dot-walk fields (link, value) when name is explicitly selected in sysparm_fields. (link and value fields cannot be explicitly added. Add root field name to select them, along with other dot-walk fields needed)
5. custom fields (user tables) do not return name values. need to find how to call these. (sysparm_display_value=all returns sys_ids values and display values. negates issue #4 and need to specify fields for names)

### API Setup Workflow
1. Get api access to ONOW (admins).
2. In ONOW, go to Rest API Explorer.
3. Run on [incident] table.
4. Select code language on page below (python). Copy code, paste into IDE (PyCharm).
5. In Python environment, install necessary packages (requests, pandas). 
6. In code, remove/change rowlimit params.
7. ServiceNow Admins must increase query timeout length. Default length is too short, for testing purposes.
