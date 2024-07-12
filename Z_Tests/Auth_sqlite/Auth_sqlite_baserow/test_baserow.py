import requests
import json

api_token = 'token' #'YOUR_API_TOKEN'
table_id = '123456' #'YOUR_TABLE_ID'
api_url = f'https://api.baserow.io/api/database/rows/table/{table_id}/'


headers = {
    'Authorization': f'Token {api_token}',
    'Content-Type': 'application/json'
}

api_url = f'https://api.baserow.io/api/database/fields/table/{table_id}/'
response = requests.get(api_url, headers=headers)
fields = response.json()

if response.status_code == 200:
    rows = response.json()
    last_row_id = rows[-1]['id']  # Get the ID of the last row

    # Delete the last row
    api_url = f'https://api.baserow.io/api/database/rows/table/{table_id}/{last_row_id}/'
    response = requests.delete(api_url, headers=headers)

    if response.status_code == 204:  # HTTP 204 means the deletion was successful
        print('Last row deleted successfully')
    else:
        print('Failed to delete last row:', response.text)
else:
    print('Failed to get data:', response.text)

# for field in fields:
#     print(field['id'], field['name'])

# # data = {
# #     'Name': 'abc',
# #     'testCold': 'aaa'
# #     # Add more fields here as needed
# # }

# if response.status_code == 200:
#     rows = response.json()
#     for row in rows:
#         print(row)
# else:
#     print('Failed to get data:', response.text)

# data = {
#     '2353700': 'abc',  # Corresponds to the 'Name' field
#     '2353747': 'aaa'   # Corresponds to the 'TestCold' field
# }

# response = requests.post(api_url, headers=headers, data=json.dumps(data))

# if response.status_code == 200:
#     print('Data pushed successfully')
# else:
#     print('Failed to push data:', response.text)