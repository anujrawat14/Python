import requests


def fetch_random_user():

    url = "https://prod-main-api-704464-00tre1p1erm.compute.instacloud-edge.com/api/v1/public/randomusers"

    response = requests.get(url)

    # print(type(response))
    # print(response)

    data = response.json()
    # converts the JSON response into Python data, usually a dictionary or list.

    if data["success"] and "data" in data:

        user_data = data["data"]["data"]
        user = user_data[0]  # first user is selected

        user_name = user["login"]["username"]

        user_country = user["location"]["country"]

        return user_name, user_country

    else:
        raise Exception("failed to fetch user data")


def main():
    try:
        user_name, user_country = fetch_random_user()
        print(f"username is : {user_name} and user belongs to  {user_country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
