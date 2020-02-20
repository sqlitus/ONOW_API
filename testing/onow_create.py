# Create ONOW ticket via API
import requests
import config

url = 'https://wfmsandbox.service-now.com/api/now/v2/table/incident?sysparm_display_value=all'
user = config.sandbox['user']
pwd = config.sandbox['pwd']
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers ,
                         data="{\"short_description\":\"some value\""
                              ",\"assignment_group\":\"Retail Support L5\""
                              ",\"assigned_to\":\"Alicea Bush\"}")

# Check for HTTP codes other than 201 Created
if response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
