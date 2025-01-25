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
