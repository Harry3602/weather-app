# Weather Insights

Weather Insights is a PyQt5-based desktop application that provides weather information for a specified location. It fetches weather data from the OpenWeatherMap API and displays it in a user-friendly interface.

## Features

- Search for weather information by city name
- Auto-detect current location and display weather
- Display weather details including temperature, humidity, wind speed, pressure, and sunrise time
- Dynamic weather icons based on current weather conditions
- Light and dark themes

## Requirements

- Python 3.9+
- PyQt5
- Requests
- Geocoder

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/weather-insights.git
    cd weather-insights
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set the OpenWeatherMap API key:
    ```sh
    export OPENWEATHER_API_KEY=your_api_key  # On Windows use `set OPENWEATHER_API_KEY=your_api_key`
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. Enter a city name in the input field and press Enter or click the search button to fetch and display the weather information.

## Project Structure

```sh
weather-insights/
├── config.py
├── images/
│   ├── cloudy.png
│   ├── default.png
│   ├── droplet.png
│   ├── mist.png
│   ├── partly_cloudy.png
│   ├── pressure.png
│   ├── rain.png
│   ├── snow.png
│   ├── sunny.png
│   ├── sunrise.png
│   ├── thunderstorm.png
│   └── wind.png
├── main.py
├── requirements.txt
├── ui/
│   └── weather_ui.py
└── weather_service.py
```
## Configuration
The configuration settings are located in the config.py file. You can customize the default units and themes.
```sh
# config.py
import os

# OpenWeatherMap API Configuration
OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY', 'your_default_api_key')

# App Configuration
APP_SETTINGS = {
    'default_units': 'metric',
    'themes': {
        'light': {
            'background': 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #E0E0E0)',
            'text_color': 'black'
        },
        'dark': {
            'background': 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2C3E50, stop:1 #34495E)',
            'text_color': 'white'
        }
    }
}
```
