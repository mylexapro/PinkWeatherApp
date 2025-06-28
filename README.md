# 🌸 Pink Weather App

A beautiful pink-themed weather application with animated effects, built with Python and Tkinter.

![App Screenshot](assets/pink_weather.png)

## ✨ Features
- Real-time weather data with 5-day forecast
- Animated weather effects (snow, rain, clouds)
- Live updating clock
- Gradient pink UI with modern widgets
- Responsive design

## ⚙️ Setup

### 1. Get API Key
🔑 Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)

### 2. Configure Environment
```bash
# Rename the example file
mv .env.example .env

# Edit the file (replace with your actual key)
nano .env

Add your key:
OPENWEATHER_API_KEY=your_api_key_here

3. Install Dependencies
pip install -r requirements.txt

🚀 Usage
python PinkWeatherApp.py

How to use:
Enter city name
Click "Get Weather"
View current conditions and forecast

📂 Files
.
├── assets/            # App icons
├── PinkWeatherApp.py  # Main application
├── .env.example       # Env template
└── .gitignore         # Git rules

🛠️ Requirements
Python 3.7+
Packages:
requests
pillow
python-dotenv

🤝 Contributing
PRs welcome! Please:
Fork the repo
Create a feature branch
Submit PR

📄 License
MIT
