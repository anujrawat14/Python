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
        user=user_data[0] #first user is selected

        user_name = user["login"]["username"]

        print(user_name)



def main():
    try:
        pass
    except:
        pass

if __name__=="__main__":
    main()
