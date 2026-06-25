# 🌤️ Weather App (CLI)

> A Python command-line weather application that fetches real-time weather data and 3-day forecasts for any city in the world — powered by Open-Meteo, completely free with no API key required.

---

## 👤 Intern Details

| Field            | Details            |
|------------------|--------------------|
| **Intern ID**    | CITS5322           |
| **Full Name**    | PREETHI S          |
| **No. of Weeks** | 4 WEEKS            |
| **Project Name** | Weather App (CLI)  |

---

## 📌 Project Scope

This project is a command-line weather application built using Python.
The app takes a city name as input from the user, fetches real-time weather
data from the Open-Meteo API, and displays it in a clean, readable format
in the terminal.

The project covers:
- Making HTTP requests to a free weather API using Python
- Parsing and extracting data from JSON responses
- Displaying current weather conditions and a 3-day forecast
- Handling errors like invalid city names and no internet connection
- Building a user-friendly CLI menu in Python

> ✅ No API key, no signup, and no cost — uses Open-Meteo which is 100% free.

---

## ✨ Features

### 🌍 Weather Features
- Search weather for **any city in the world**
- 🌡️ Current **temperature** and **feels like** temperature
- 💧 **Humidity** percentage
- 💨 **Wind speed** and wind direction
- 📊 **Atmospheric pressure**
- ☀️ Weather **condition with emoji** (Clear, Rainy, Stormy etc.)
- 📅 **3-day forecast** with high / low temperatures
- 🌅 **Sunrise and Sunset** times per day
- 🌧️ **Rainfall amount** in mm (in forecast)

### ⚙️ Technical Features
- ✅ No API key needed
- ✅ No signup required
- ✅ 100% Free — powered by Open-Meteo
- ✅ Real live weather data from the internet
- ✅ Error handling — wrong city name, no internet
- ✅ Timeout handling — if server is slow
- ✅ Clean CLI menu with numbered options
- ✅ Auto timezone — shows correct local time per city
- ✅ Supports all countries worldwide

### ☁️ Weather Conditions Supported
| Condition | Emoji |
|-----------|-------|
| Clear Sky | ☀️ |
| Partly Cloudy | ⛅ |
| Overcast | ☁️ |
| Fog | 🌫️ |
| Light / Moderate / Heavy Rain | 🌧️ |
| Snow | ❄️ |
| Thunderstorm | ⛈️ |
| Snow Showers | 🌨️ |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming language |
| requests | Fetch data from Open-Meteo API |
| JSON | Parse API response data |
| DateTime | Format date and time display |
| Open-Meteo Geocoding API | Convert city name to coordinates |
| Open-Meteo Forecast API | Fetch real-time weather data |

---

## 📖 Documentation

### Project Structure
```
weather-app-cli/
│
├── weather_app.py       # Main application file
└── README.md            # Project documentation
└── task 2 output images # output screenshots
```

### How the Code Works

#### 1. WEATHER_CODES (Dictionary)
Open-Meteo returns a number called a weather code (e.g. 0 = Clear Sky, 63 = Rain).
This dictionary maps every code to a human-readable condition and an emoji.

#### 2. get_coordinates(city_name)
Calls the Open-Meteo Geocoding API with the city name.
Returns the city's latitude, longitude, country, and timezone.
If the city is not found, returns None.

#### 3. get_weather(latitude, longitude, timezone)
Calls the Open-Meteo Forecast API with the coordinates.
Requests current weather + 4-day daily forecast data.
Returns the full JSON response.

#### 4. display_current_weather(city_info, weather_data)
Extracts current weather values from the JSON response
and prints them in a clean, formatted layout in the terminal.

#### 5. display_forecast(weather_data)
Loops through the next 3 days of forecast data
and prints high/low temperature, condition, rain, sunrise, and sunset
for each day.

#### 6. main()
Runs the CLI menu in a loop using while True.
Takes user input and calls the correct functions based on choice.
Handles invalid inputs gracefully.


### Error Handling
- **City not found** — shows a friendly message and asks to re-enter
- **No internet** — catches `ConnectionError` and informs the user
- **Timeout** — catches `Timeout` if the server takes too long
- **Invalid menu choice** — asks user to enter 1, 2, or 3 again

---

## 📚 Python Concepts Used

| Concept | Where Used |
|---------|------------|
| `requests` library | Fetch data from Open-Meteo API |
| JSON parsing | Read and extract weather data |
| `try / except` | Handle connection and timeout errors |
| Dictionary | Weather code to condition mapping |
| f-strings | Format terminal output cleanly |
| `datetime` | Format date and time display |
| `while True` loop | Keep CLI menu running |
| Functions | Modular, reusable code structure |

---

## 📚 Concepts Learned

- Making API calls in Python using `requests`
- Parsing JSON data from web responses
- Error and exception handling
- Building interactive CLI menus
- Working with real-world weather data
- Using free public APIs without authentication

---
