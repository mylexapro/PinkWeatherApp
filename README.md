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

## ⚙️ Configure Environment

1. Rename the example file:
```bash
mv .env.example .env
```

2. Edit the file with your API key:
```bash
nano .env  # or use your preferred text editor
```

3. Add your OpenWeatherMap API key:
```ini
OPENWEATHER_API_KEY=your_api_key_here
```
## 📦 Install Dependencies

1. First install Python 3.7+ if you haven't already:
```bash
python --version  # verify installation
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. If you don't have a requirements.txt yet, install packages manually:
```bash
pip install requests pillow python-dotenv
```

💡 **Troubleshooting Tips**:
- Use `pip3` instead of `pip` if needed
- Add `--user` flag if getting permission errors
- On Linux/macOS, you may need `sudo` for global install
