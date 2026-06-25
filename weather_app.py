# ============================================
# WEATHER APP - CLI VERSION
# Python Internship - Task 2
# Uses Open-Meteo API (No API Key Needed!)
# ============================================

import requests
from datetime import datetime

# ============================================
# WEATHER CODE DESCRIPTIONS
# Open-Meteo returns a number (weather code)
# This dictionary converts it to readable text
# ============================================
WEATHER_CODES = {
    0:  ("Clear Sky",            "☀️"),
    1:  ("Mainly Clear",         "🌤️"),
    2:  ("Partly Cloudy",        "⛅"),
    3:  ("Overcast",             "☁️"),
    45: ("Foggy",                "🌫️"),
    48: ("Icy Fog",              "🌫️"),
    51: ("Light Drizzle",        "🌦️"),
    53: ("Moderate Drizzle",     "🌦️"),
    55: ("Heavy Drizzle",        "🌧️"),
    61: ("Slight Rain",          "🌧️"),
    63: ("Moderate Rain",        "🌧️"),
    65: ("Heavy Rain",           "🌧️"),
    71: ("Slight Snowfall",      "❄️"),
    73: ("Moderate Snowfall",    "❄️"),
    75: ("Heavy Snowfall",       "❄️"),
    77: ("Snow Grains",          "🌨️"),
    80: ("Slight Rain Showers",  "🌦️"),
    81: ("Moderate Rain Showers","🌧️"),
    82: ("Violent Rain Showers", "⛈️"),
    85: ("Slight Snow Showers",  "🌨️"),
    86: ("Heavy Snow Showers",   "🌨️"),
    95: ("Thunderstorm",         "⛈️"),
    96: ("Thunderstorm w/ Hail", "⛈️"),
    99: ("Thunderstorm w/ Hail", "⛈️"),
}


# ============================================
# STEP 1: GET CITY COORDINATES
# Open-Meteo needs latitude & longitude
# We use their free Geocoding API to get it
# ============================================
def get_coordinates(city_name):
    """
    Takes a city name and returns its latitude and longitude.
    Uses Open-Meteo's free Geocoding API — no key needed.
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if "results" not in data or len(data["results"]) == 0:
            return None  # city not found

        result = data["results"][0]
        return {
            "name":      result["name"],
            "country":   result.get("country", ""),
            "latitude":  result["latitude"],
            "longitude": result["longitude"],
            "timezone":  result.get("timezone", "auto")
        }

    except requests.exceptions.ConnectionError:
        print("\n  ❌ No internet connection. Please check your network.")
        return None
    except requests.exceptions.Timeout:
        print("\n  ❌ Request timed out. Try again.")
        return None
    except Exception as e:
        print(f"\n  ❌ Error: {e}")
        return None


# ============================================
# STEP 2: GET WEATHER DATA
# Pass lat/lon to Open-Meteo weather API
# ============================================
def get_weather(latitude, longitude, timezone):
    """
    Fetches current weather and 3-day forecast
    from Open-Meteo using coordinates.
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,apparent_temperature,relative_humidity_2m,"
        f"wind_speed_10m,wind_direction_10m,weather_code,surface_pressure,visibility"
        f"&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,sunrise,sunset"
        f"&timezone={timezone}"
        f"&forecast_days=4"
    )

    try:
        response = requests.get(url, timeout=10)
        return response.json()

    except requests.exceptions.ConnectionError:
        print("\n  ❌ No internet connection.")
        return None
    except Exception as e:
        print(f"\n  ❌ Error fetching weather: {e}")
        return None


# ============================================
# DISPLAY: CURRENT WEATHER
# ============================================
def display_current_weather(city_info, weather_data):
    """Prints the current weather in a clean format."""

    current = weather_data["current"]

    code        = current.get("weather_code", 0)
    condition, icon = WEATHER_CODES.get(code, ("Unknown", "🌡️"))
    temp        = current.get("temperature_2m", "N/A")
    feels_like  = current.get("apparent_temperature", "N/A")
    humidity    = current.get("relative_humidity_2m", "N/A")
    wind_speed  = current.get("wind_speed_10m", "N/A")
    wind_dir    = current.get("wind_direction_10m", "N/A")
    pressure    = current.get("surface_pressure", "N/A")
    now         = datetime.now().strftime("%d %b %Y  |  %I:%M %p")

    print("\n" + "=" * 52)
    print(f"  🌍  {city_info['name']}, {city_info['country']}")
    print(f"  🕐  {now}")
    print("=" * 52)
    print(f"  {icon}  {condition}")
    print(f"  🌡️   Temperature   :  {temp}°C")
    print(f"  🤔  Feels Like    :  {feels_like}°C")
    print(f"  💧  Humidity      :  {humidity}%")
    print(f"  💨  Wind Speed    :  {wind_speed} km/h")
    print(f"  🧭  Wind Direction:  {wind_dir}°")
    print(f"  📊  Pressure      :  {pressure} hPa")
    print("=" * 52)


# ============================================
# DISPLAY: 3-DAY FORECAST
# ============================================
def display_forecast(weather_data):
    """Prints a 3-day weather forecast."""

    daily = weather_data.get("daily", {})

    if not daily:
        print("  No forecast data available.")
        return

    dates     = daily.get("time", [])
    codes     = daily.get("weather_code", [])
    max_temps = daily.get("temperature_2m_max", [])
    min_temps = daily.get("temperature_2m_min", [])
    rains     = daily.get("precipitation_sum", [])
    sunrises  = daily.get("sunrise", [])
    sunsets   = daily.get("sunset", [])

    print("\n  📅  3-DAY FORECAST")
    print("  " + "-" * 48)

    # Skip index 0 (today), show next 3 days
    for i in range(1, min(4, len(dates))):
        code = codes[i] if i < len(codes) else 0
        condition, icon = WEATHER_CODES.get(code, ("Unknown", "🌡️"))

        date     = dates[i] if i < len(dates) else "N/A"
        max_t    = max_temps[i] if i < len(max_temps) else "N/A"
        min_t    = min_temps[i] if i < len(min_temps) else "N/A"
        rain     = rains[i] if i < len(rains) else 0
        sunrise  = sunrises[i][11:16] if i < len(sunrises) else "N/A"
        sunset   = sunsets[i][11:16] if i < len(sunsets) else "N/A"

        # Format date nicely
        try:
            day_name = datetime.strptime(date, "%Y-%m-%d").strftime("%A, %d %b")
        except:
            day_name = date

        print(f"\n  {icon}  {day_name}")
        print(f"      Condition : {condition}")
        print(f"      High / Low: {max_t}°C  /  {min_t}°C")
        print(f"      Rain      : {rain} mm")
        print(f"      Sunrise   : {sunrise}  |  Sunset: {sunset}")

    print("\n  " + "-" * 48)


# ============================================
# DISPLAY: WIND DIRECTION
# ============================================
def wind_direction_label(degrees):
    """Converts wind degrees to compass direction."""
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = round(degrees / 45) % 8
    return directions[index]


# ============================================
# MAIN MENU
# ============================================
def show_menu():
    print("\n" + "-" * 52)
    print("         🌤️  WEATHER APP  (Powered by Open-Meteo)")
    print("-" * 52)
    print("  1.  Check Current Weather")
    print("  2.  Check Weather + 3-Day Forecast")
    print("  3.  Exit")
    print("-" * 52)


# ============================================
# MAIN PROGRAM
# ============================================
def main():
    print("\n  Welcome to the Weather App!")
    print("  Powered by Open-Meteo — Free, No API Key Needed 🌍")

    while True:
        show_menu()
        choice = input("  Enter your choice (1-3): ").strip()

        if choice == "1":
            city = input("  Enter city name: ").strip()
            if not city:
                print("  ⚠  Please enter a city name.")
                continue

            print(f"\n  🔍 Searching for '{city}'...")
            city_info = get_coordinates(city)

            if not city_info:
                print(f"  ❌ City '{city}' not found. Please check the spelling.")
                continue

            print(f"  ✅ Found: {city_info['name']}, {city_info['country']}")
            print("  ⏳ Fetching weather data...")

            weather = get_weather(city_info["latitude"], city_info["longitude"], city_info["timezone"])

            if weather:
                display_current_weather(city_info, weather)

        elif choice == "2":
            city = input("  Enter city name: ").strip()
            if not city:
                print("  ⚠  Please enter a city name.")
                continue

            print(f"\n  🔍 Searching for '{city}'...")
            city_info = get_coordinates(city)

            if not city_info:
                print(f"  ❌ City '{city}' not found. Please check the spelling.")
                continue

            print(f"  ✅ Found: {city_info['name']}, {city_info['country']}")
            print("  ⏳ Fetching weather data...")

            weather = get_weather(city_info["latitude"], city_info["longitude"], city_info["timezone"])

            if weather:
                display_current_weather(city_info, weather)
                display_forecast(weather)

        elif choice == "3":
            print("\n  Goodbye! Stay weather-ready! 🌈\n")
            break

        else:
            print("  ❌ Invalid choice. Enter 1, 2, or 3.")


# ============================================
# RUN
# ============================================
if __name__ == "__main__":
    main()