# APi key  c27f208a45e04709936113746262910
#  weather api https://api.weatherapi.com/v1/current.json?key=c27f208a45e04709936113746262910&q=London

import requests

API_key = "c27f208a45e04709936113746262910"
Base_url = "https://api.weatherapi.com/v1/current.json"


def print_data(data):

    print(f"City  {data["location"]["name"]} in {data["location"]["country"]} ")
    print()
    print("*" * 10)

    print(f"Temperature is {data["current"]["temp_c"]} degree celsius ")
    print(f"Condition is {data["current"]["condition"]["text"]} ")

    print("Humidity:", data["current"]["humidity"], "%")
    print("Wind Speed:", data["current"]["wind_kph"], "km/h")

    print("*" * 10)


def weather_API_handler(city):

    params = {"key": API_key, "q": city}

    try:
        response = requests.get(Base_url, params=params, timeout=10)

        response.raise_for_status()  # raise exception for http errors

        data = response.json()

        # information to show the user
        print_data(data)

    except requests.exceptions.HTTPError:
        print("HTTP error:", response.text)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

    except (KeyError, ValueError, TypeError):
        print("Invalid or unexpected API response.")


def main():
    print("This is a weather App || Rawat")

    city = input("Enter name of your city : ").strip()  # remove unnecessary spaces

    if city:
        weather_API_handler(city)
    else:
        print("city name cant be empty")


if __name__ == "__main__":
    main()
