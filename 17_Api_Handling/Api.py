import requests


response = requests.get("http\
s://prod-main-api-704464-00tre1\
p1erm.compute.instacloud-edge.c\
om/api/v1/public/randomusers?pa\
ge=1&limit=10")

data = response.json()
# we get response in

print(data)
