# ONOW_API

Purpose: Reference for establishing ONOW connection to SNOW API.

### Resources
- [Explore the REST API for a table](https://docs.servicenow.com/bundle/madrid-application-development/page/integrate/inbound-rest/task/explore-rest-api-for-table.html)
- [ODBC driver](https://docs.servicenow.com/bundle/newyork-application-development/page/integrate/odbc-driver/concept/c_ODBCDriver.html)

### Environment
Pycharm. Python 3.8+. Windows 10.

### Notes
Testing in sandbox initially. Will need access to prod.
Current Version: 2.

### Issues addressed (& resolution)
1. incorrect row amt (admin, sec permission)
2. larger query timeout (admin, execution length)
3. missing columns (admin, sec permission)
4. missing dot-walk fields when one is selected.

### API Setup Workflow
1. get api access to ONOW.
2. In ONOW, go to Rest API Explorer.
3. Run on [incident] table
4. Select code language below (python). Copy code, paste into IDE (PyCharm).
5. Install necessary packages (requests, pandas). 
6. In code, change rowlimit params.