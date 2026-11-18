# Basic Weather App — Beginner Tier

## Objective
Fetch and display current weather for a city using a weather API.

## Features
- Accepts a city name and checks for empty input.
- Calls the OpenWeatherMap Current Weather API.
- Parses the JSON response.
- Displays temperature in Celsius and Fahrenheit, humidity, condition and wind speed.
- Handles city-not-found, invalid API key, timeout and network errors.

## Setup on Windows
1. Create a free API key at https://openweathermap.org/api.
2. Open Command Prompt in this folder.
3. Install the dependency: `py -m pip install -r requirements.txt`
4. Run: `py main.py`
5. Enter the city and your API key when prompted.

Keep your API key private. Do not upload it to GitHub or include it in screenshots. New API keys may take time to activate.
