import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("WEATHER_API_URL")

if not API_KEY or not BASE_URL:
    raise ValueError("Missing API configuration. Check your .env file.")


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
    print(f"💧 Humidity   : {current['humidity']}%")
    print(f"💨 Wind Speed : {current['wind_kph']} km/h")

    print("\n" + "═" * 42)
    print("          Have a great day! ✨")
    print("═" * 42 + "\n")


def weather_API_handler(city):

    params = {"key": API_KEY, "q": city}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

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
