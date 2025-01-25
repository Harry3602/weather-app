import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from weather_service import WeatherService
import config

class WeatherApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_theme = 'dark'
        self.setupUi()

    def setupUi(self):
        self.setObjectName("WeatherApp")
        self.setFixedSize(500, 700)  # Increased width from 400 to 500
        self.setWindowTitle("Weather Insights")

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Main Layout
        main_layout = QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Search Container
        search_container = QHBoxLayout()
        
        # Location Input
        self.location_input = QtWidgets.QLineEdit()
        self.location_input.setPlaceholderText("Enter city name...")
        self.location_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border-radius: 15px;
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                border: 1px solid rgba(255, 255, 255, 0.3);
            }
        """)
        self.location_input.returnPressed.connect(self.search)
        
        # Search Button (Restored)
        self.search_button = QtWidgets.QPushButton("🔍")  # Emoji search icon
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 10px;
                color: white;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
        """)
        self.search_button.clicked.connect(self.search)
        
        search_container.addWidget(self.location_input)
        search_container.addWidget(self.search_button)
        
        # City and Temperature Display
        self.city_label = QLabel("Weather Insights")
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        
        # Weather Icon
        self.weather_icon = QLabel()
        self.weather_icon.setAlignment(Qt.AlignCenter)
        
        # Temperature Label
        self.temp_label = QLabel()
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.temp_label.setStyleSheet("font-size: 48px; font-weight: bold; color: white;")
        
        # Description Label
        self.description_label = QLabel()
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setStyleSheet("font-size: 18px; color: rgba(255,255,255,0.7);")
        
        # Weather Details Grid
        details_grid = QHBoxLayout()
        detail_configs = [
            ('humidity_label', 'Humidity', 'droplet.png'),
            ('wind_label', 'Wind', 'wind.png'),
            ('pressure_label', 'Pressure', 'pressure.png'),
            ('sunrise_label', 'Sunrise', 'sunrise.png')
        ]
        
        for attr, text, icon in detail_configs:
            detail_widget = self.create_detail_widget(text, icon)
            setattr(self, attr, detail_widget['value'])
            details_grid.addWidget(detail_widget['container'])

        # Add Widgets to Main Layout
        main_layout.addLayout(search_container)
        main_layout.addWidget(self.city_label)
        main_layout.addWidget(self.weather_icon)
        main_layout.addWidget(self.temp_label)
        main_layout.addWidget(self.description_label)
        main_layout.addLayout(details_grid)

        # Apply Initial Theme
        self.apply_theme()
        self.auto_detect_location()


    def search(self):
        location = self.location_input.text().strip()
        if not location:
            self.show_error("Please enter a location!")
            return

        weather = WeatherService.fetch_weather(location)
        
        if "error" in weather:
            self.show_error(f"Error: {weather['error']}")
            return

        self.update_weather_display(weather)

    def update_weather_display(self, weather):
    # Update labels with weather data
        self.city_label.setText(weather.get('name', 'Unknown Location'))
        self.temp_label.setText(f"{weather['temp']}°C")
        description = weather['description'].lower()
        self.description_label.setText(description.capitalize())
        
        # Update detail labels
        self.humidity_label.setText(f"{weather['humidity']}%")
        self.wind_label.setText(f"{weather['wind_speed']} m/s")
        self.pressure_label.setText(f"{weather['pressure']} hPa")
        self.sunrise_label.setText(weather['sunrise'])
        
        # Weather icon mapping
        icon_mapping = {
            'clear sky': 'sunny.png',
            'few clouds': 'partly_cloudy.png',
            'scattered clouds': 'cloudy.png',
            'broken clouds': 'cloudy.png',
            'overcast clouds': 'cloudy.png',
            'rain': 'rain.png',
            'light rain': 'rain.png',
            'moderate rain': 'rain.png',
            'heavy rain': 'rain.png',
            'thunderstorm': 'thunderstorm.png',
            'snow': 'snow.png',
            'mist': 'mist.png',
            'fog': 'mist.png'
        }
        
        # Select icon, default to default.png if not found
        icon_file = icon_mapping.get(description, 'default.png')
        icon_path = os.path.join('images', icon_file)
        
        # Set weather icon
        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path).scaled(
                200, 200, 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            self.weather_icon.setPixmap(pixmap)
            self.weather_icon.setAlignment(Qt.AlignCenter)
        else:
            print(f"Icon not found: {icon_path}")

    def show_error(self, message):
        # Handle and display errors
        self.description_label.setText(message)
        self.temp_label.clear()
        for label in [self.humidity_label, self.wind_label, 
                      self.pressure_label, self.sunrise_label]:
            label.clear()

    def create_detail_widget(self, text, icon_name):
        container = QVBoxLayout()
        container.setSpacing(5)
        container.setAlignment(Qt.AlignCenter)
        
        # Icon
        icon_label = QLabel()
        icon_path = os.path.join('images', icon_name)
        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path).scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(pixmap)
            icon_label.setAlignment(Qt.AlignCenter)
        
        # Text Labels
        title_label = QLabel(text)
        title_label.setStyleSheet("color: rgba(255,255,255,0.6); font-size: 12px;")
        title_label.setAlignment(Qt.AlignCenter)
        
        value_label = QLabel()
        value_label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        value_label.setAlignment(Qt.AlignCenter)
        
        container.addWidget(icon_label)
        container.addWidget(title_label)
        container.addWidget(value_label)
        
        widget_container = QtWidgets.QWidget()
        widget_container.setLayout(container)
        
        return {
            'container': widget_container,
            'value': value_label
        }
    
    def apply_theme(self):
        theme = config.APP_SETTINGS['themes'][self.current_theme]
        background_gradient = (
            "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, "
            "stop:0 #2C3E50, stop:1 #34495E);"
        )
        self.setStyleSheet(f"""
            QMainWindow {{
                {background_gradient}
            }}
            QWidget {{
                background: transparent;
                color: white;
            }}
        """)

    def auto_detect_location(self):
        location = WeatherService.get_current_location()
        if location:
            self.location_input.setText(location)
            self.search()

def main():
    app = QtWidgets.QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()