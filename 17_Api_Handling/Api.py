import requests


def fetch_random_user():

    url = "https://prod-main-api-704464-00tre1p1erm.compute.instacloud-edge.com/api/v1/public/randomusers?page=1&limit=10"

    response = requests.get(url)

    # print(type(response))

    #print(response)

    data = response.json()
    # converts the JSON response into Python data, usually a dictionary or list.

    if data["success"] and "data" in data:
        user_data = data["data"]

        # Access the list of users
        # users = user_data["data"]

        # # Access the first user in the list
        # first_name = users[0]["name"]["first"]

        # print(first_name)


fetch_random_user()

# data = response.json()

# print(data)
