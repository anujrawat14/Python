import requests

response = requests.get(
    "https://prod-main-api-704464-00tre1\p1erm.compute.instacloud-edge.com/api/v1/public/randomusers?page=1&limit=10"
)

data = response.json()
# converts the JSON response into Python data, usually a dictionary or list.

print(data)
