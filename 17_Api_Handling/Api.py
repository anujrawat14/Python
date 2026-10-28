import requests


def fetch_random_user():

    url = "https://prod-main-api-704464-00tre1p1erm.compute.instacloud-edge.com/api/v1/public/randomusers?page=1&limit=10"

    response = requests.get(url)

    # print(type(response))

    print(response)

    data = response.json()
    # converts the JSON response into Python data, usually a dictionary or list.

    if data["success"] and "data" in data:
        print(data)






fetch_random_user()

# data = response.json()

# print(data)
