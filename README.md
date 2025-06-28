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

## 🚀 Usage

1. Run the application:
```bash
python PinkWeatherApp.py
```

2. Application interface:
```
1. Enter city name in the text field
2. Click "Get Weather" button
3. View current weather and 5-day forecast
```

3. Example workflow:
```bash
# After launching the app:
1. Type "New York" in the city field
2. Press Enter or click the pink button
3. See animated weather effects appear
```

🌈 **Pro Tips**:
- Double-click the city field to clear previous entries
- The app automatically updates the time every second
- Weather animations change based on current conditions
- Window is resizable if you need more space

  
