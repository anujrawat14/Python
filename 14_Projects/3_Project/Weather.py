# APi key  c27f208a45e04709936113746262910
#  weather api https://api.weatherapi.com/v1/current.json?key=c27f208a45e04709936113746262910&q=London

import requests

API_key = "c27f208a45e04709936113746262910"
Base_url = "https://api.weatherapi.com/v1/current.json"


def print_data(data):

    location = data["location"]
    current = data["current"]

    condition = current["condition"]["text"].lower()

    # Choose an emoji based on weather condition
    if "sun" in condition or "clear" in condition:
        icon = "☀️"
    elif "rain" in condition or "drizzle" in condition:
        icon = "🌧️"
    elif "cloud" in condition or "overcast" in condition:
        icon = "☁️"
    elif "snow" in condition or "ice" in condition:
        icon = "❄️"
    elif "thunder" in condition:
        icon = "⛈️"
    elif "mist" in condition or "fog" in condition:
        icon = "🌫️"
    else:
        icon = "🌤️"

    print("\n" + "═" * 42)
    print("          🌍 WEATHER REPORT")
    print("═" * 42)

    print(f"\n📍 Location   : {location['name']}, {location['country']}")
    print(f"{icon} Condition  : {current['condition']['text']}")
    print(f"🌡️ Temperature: {current['temp_c']}°C")
    # print(f"💧 Humidity   : {current['humidity']}%")
    # print(f"💨 Wind Speed : {current['wind_kph']} km/h")

    print("\n" + "═" * 42)
    print("          Have a great day! ✨")
    print("═" * 42 + "\n")


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
