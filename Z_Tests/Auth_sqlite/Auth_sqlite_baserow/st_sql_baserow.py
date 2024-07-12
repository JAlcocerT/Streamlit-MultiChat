
#https://baserow.io/user-docs

import requests #https://requests.readthedocs.io/en/latest/


requests.get(
    "https://api.baserow.io",
    headers={
        "Authorization": "Token YOUR_DATABASE_TOKEN"
    }
)