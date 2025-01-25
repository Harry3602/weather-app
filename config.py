import os

# OpenWeatherMap API Configuration
OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY', '587ac082e95894b044f613487273b578')

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