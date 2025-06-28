# 🌸 Pink Weather App v1.0.0

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

## 📂 File Structure

Here's the complete project layout:

```
PinkWeatherApp/
├── assets/                  # Contains all graphical assets
│   ├── pink_weather.ico     # Application icon (Windows)
│   └── pink_weather.png     # Application icon (macOS/Linux)
├── PinkWeatherApp.py        # Main application source code
├── .env.example             # Environment template file
├── .gitignore               # Git ignore rules
└── README.md                # This documentation file
```

🔍 **Key Files Explained**:
- `PinkWeatherApp.py`: Contains all application logic and GUI code
- `.env.example`: Template for your environment variables
- `assets/`: Stores all icon files (keep this folder intact)

⚠️ **Important Notes**:
- Never delete the `assets/` folder
- The `.env` file will be created during setup
- All files must remain in their original locations

## 🛠️ Requirements

### Core Requirements
```bash
Python 3.7+ (Recommended: 3.9+)
```

### Python Packages
```bash
requests >= 2.28.0      # For API calls
Pillow >= 9.4.0        # For image handling
python-dotenv >= 0.21  # For environment variables
```

### Optional (For Development)
```bash
tkinter    # Usually included with Python
black      # Code formatting
flake8     # Linting
```

💻 **System Compatibility**:
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu 20.04+, Fedora, etc.)
- ✅ Raspberry Pi OS

📌 **Installation Notes**:
```bash
# Verify Python version
python --version

# Verify pip installation
pip --version
```

## 🤝 Contributing

### How to Contribute:
1. Fork the repository:
```bash
gh repo fork yourusername/PinkWeatherApp
```

2. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes:
```bash
git commit -m "Add: your meaningful message"
```

4. Push to your branch:
```bash
git push origin feature/your-feature-name
```

5. Open a Pull Request

### Contribution Guidelines:
```markdown
- Keep code style consistent
- Update documentation when needed
- Write clear commit messages
- Test changes thoroughly
```

💡 **Good First Issues**:
- Improve error handling
- Add more weather animations
- Enhance mobile compatibility
- Create additional themes

📌 **Note**:
```bash
# Run linter before submitting PR
flake8 PinkWeatherApp.py
```

## 📜 License

### Usage Rights
```plaintext
This project has no license restrictions.
You are free to:
- Use the code for any purpose
- Modify and adapt the script
- Share your changes
- Use commercially or personally
```

### Suggested Attribution (Optional)
```markdown
If you find this useful, consider:
- Giving the repo a ⭐
- Mentioning the original project
- Sharing your improvements
```

🔄 **Redistribution Notice**:
```bash
# When sharing modified versions:
1. Clearly state it's a modified version
2. Consider opening a PR with your improvements
3. Don't claim original authorship
```

💡 **About Open Source**:
```plaintext
While not required, contributing back
helps the project grow for everyone!
```

## 🌟 Enjoy the App!

### Need Help?
```bash
# Common fixes:
1. API not working? Check your .env file
2. Missing icons? Verify assets/ folder exists
3. GUI issues? Try reinstalling tkinter:
   sudo apt-get install python3-tk  # Linux
```

### Share Your Version
```markdown
Tag me on GitHub if you:
- Created a cool theme variation
- Added new weather animations
- Ported to another language/framework
```

🎉 **Final Notes**:
```plaintext
This project was made with fun in mind.
Feel free to make it your own!
```
