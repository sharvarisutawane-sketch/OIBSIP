import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"

def main():
    print("=" * 38)
    print("          BASIC WEATHER APP")
    print("=" * 38)

    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    if not api_key:
        print("API key cannot be empty.")
        return

    try:
        response = requests.get(
            API_URL,
            params={"q": city, "appid": api_key, "units": "metric"},
            timeout=15
        )

        if response.status_code == 401:
            print("Invalid API key. Please check your key.")
            return
        if response.status_code == 404:
            print("City not found. Please check the spelling.")
            return

        response.raise_for_status()
        data = response.json()

        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9 / 5) + 32
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        print("\\nWeather in", data["name"])
        print("-" * 30)
        print(f"Temperature: {temperature_c:.1f} °C")
        print(f"Temperature: {temperature_f:.1f} °F")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.Timeout:
        print("The request timed out. Please try again.")
    except requests.RequestException as error:
        print("Network or API error:", error)
    except (KeyError, TypeError):
        print("The weather service returned an unexpected response.")

if __name__ == "__main__":
    main()
