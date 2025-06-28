# ===== PINK WEATHER APP =====

#===== IMPORTS =====
# Standard Library
import os
import sys
import io
import random
import time
from datetime import datetime
from urllib.request import urlopen

# GUI
import tkinter as tk
from tkinter import ttk

# Image Processing
from PIL import Image, ImageTk  # The main working imports

# Web Requests
import requests

# Environment
from dotenv import load_dotenv

# ===== CONSTANTS =====
load_dotenv()  # This loads the .env file before we use os.getenv()

# Colors
PINK_TEXT = "#5E2D50"  # Dark pink/mauve for better contrast
PINK_BTN = "#FF69B4"   # Brighter pink button
BTN_TEXT = "white"     # White text on buttons
PINK_BG = "#FFC0CB"  # This is a light pink color code
FORECAST_BG = "#FFECF5"  # Lighter pink for forecast cards
FORECAST_TEXT = "#A83766"  # Deep pink text

#Fonts
FONT_NAME = "Verdana"

# Modern Transparent Widgets
transparent = "#FFD1DC"  # Slightly transparent pink

#API Key
API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Make sure this line exists

# Weather Icons
ICON_URL = "https://openweathermap.org/img/wn/{icon_code}@2x.png"

# Weather Effects
WEATHER_EFFECTS = {
    "snow": {"color": "#FFFFFF", "symbol": "❄", "speed": 2},  # Animated Snow
    "rain": {"color": "#A5D8FF", "symbol": "🌧", "speed": 3},  # Animated Rain
    "clouds": {"color": "#E6F0FF", "symbol": "☁", "speed": 1}  # Animated Clouds
}


# ===== FUNCTIONS =====

# Path Helper Function
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # noinspection SpellCheckingInspection
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    except (AttributeError, OSError) as e:
        # Only catch specific exceptions we expect
        print(f"Warning: Falling back to default path ({str(e)})")
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Icon Loading Function
def load_app_icon():
    """Super reliable icon loader with detailed debugging"""
    print("\n=== Trying to load app icon ===")

    # Possible locations to check (both ICO and PNG)
    attempts = [
        ("ICO", os.path.join("assets", "pink_weather.ico")),
        ("ICO", os.path.join(os.path.dirname(__file__), "pink_weather.ico")),
        ("PNG", os.path.join("assets", "pink_weather.png")),
        ("PNG", os.path.join(os.path.dirname(__file__), "pink_weather.png")),
    ]

    for file_type, path in attempts:
        full_path = resource_path(path) if "assets" in path else path
        try:
            if os.path.exists(full_path):
                print(f"Trying {file_type} at: {full_path}")
                if file_type == "ICO":
                    app.iconbitmap(full_path)
                    print("✓ Successfully loaded ICO icon!")
                    return True
                else:  # PNG
                    img = tk.PhotoImage(file=full_path)
                    app.iconphoto(True, img)
                    print("✓ Successfully loaded PNG icon!")
                    return True
            else:
                print(f"File not found: {full_path}")
        except Exception as e:
            print(f"Failed to load {file_type}: {str(e)}")

    print("⚠ Could not load any icon - app will run without one")
    return False

# Live Clock Function
def update_clock() -> None:
    """Updates the clock label every second"""
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=f"🕒 {current_time}")
    clock_label.after(1000, update_clock)  # type: ignore


# Weather Function
def fetch_weather():
    city = city_entry.get()

    try:
        # 1. Fetch weather data
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
        response = requests.get(url)
        data = response.json()
        weather_main = data['weather'][0]['main'].lower()

        # 2. Handle animations
        for anim in animations.values():
            anim.stop()
        canvas.delete("weather")

        if weather_main in animations:
            animations[weather_main].start()

        # 3. Update text display
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description'].title()
        last_updated = datetime.now().strftime("%b %d at %I:%M %p")

        result_label.config(
            text=f"{temp}°F • {weather_desc}\n🕒 Updated: {last_updated}",
            font=(FONT_NAME, 14),
            foreground=PINK_TEXT,
            background=PINK_BG,
            justify="center"
        )

        # 4. TYPE-ANNOTATED IMAGE HANDLING
        icon_code = data['weather'][0]['icon']
        icon_url = ICON_URL.format(icon_code=icon_code)

        # Get and process image
        with urlopen(icon_url) as response:
            pil_image = Image.open(io.BytesIO(response.read()))

        resized_image = pil_image.resize((100, 100), Image.Resampling.LANCZOS)
        weather_photo = ImageTk.PhotoImage(image=resized_image)

        # Update display (with PyCharm suppression)
        # noinspection PyTypeChecker
        icon_label.config(image=weather_photo)
        icon_label.__weather_photo = weather_photo  # Special storage

        # 5. Show forecast
        show_forecast(city)

    except Exception as e:
        result_label.config(
            text=f"Error: {str(e)}",
            foreground="#FF0000"
        )


# 5-Day Forecast Function
def show_forecast(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=imperial"
        response = requests.get(url, timeout=10)
        data = response.json()

        # Clear previous forecast cards
        for child_widget in forecast_frame.winfo_children():
            child_widget.destroy()

        # Get unique dates from forecast data
        forecast_dates = []
        for forecast in data['list']:
            date = forecast['dt_txt'].split()[0]  # Extract just the date part
            if date not in forecast_dates:
                forecast_dates.append(date)
                if len(forecast_dates) == 5:  # Only need 5 days
                    break

        # Display one forecast per day (using noon forecasts when available)
        for i, date in enumerate(forecast_dates):
            # Find a forecast for this date (preferably near noon)
            for forecast in data['list']:
                forecast_date, forecast_time = forecast['dt_txt'].split()
                if forecast_date == date:
                    # Prefer forecasts between 11am-2pm
                    if "12:00:00" in forecast_time or (i == 0 and forecast_time >= "06:00:00"):
                        temp = forecast['main']['temp']
                        desc = forecast['weather'][0]['description']
                        icon_code = forecast['weather'][0]['icon']

                        # Format date as "Tue Jun 28"
                        date_obj = datetime.strptime(date, "%Y-%m-%d")
                        formatted_date = date_obj.strftime("%a %b %d")

                        # Create forecast card
                        card = tk.Frame(forecast_frame, bg=FORECAST_BG, padx=5, pady=5)
                        card.grid(row=0, column=i, padx=5)

                        # Date label
                        tk.Label(card, text=formatted_date, bg=FORECAST_BG, fg=FORECAST_TEXT,
                                 font=(FONT_NAME, 10, "bold")).pack()

                        # Weather icon
                        icon_url = ICON_URL.format(icon_code=icon_code)
                        with urlopen(icon_url) as response:
                            icon_data = response.read()
                        pil_img = Image.open(io.BytesIO(icon_data))
                        pil_img = pil_img.resize((50, 50), Image.Resampling.LANCZOS)
                        forecast_icon_img = ImageTk.PhotoImage(pil_img)  # Changed variable name

                        # Create forecast icon label with unique name
                        forecast_icon_label = tk.Label(card, bg=FORECAST_BG)  # Changed variable name
                        # noinspection PyTypeChecker
                        forecast_icon_label.config(image=forecast_icon_img)  # Updated reference
                        forecast_icon_label.image = forecast_icon_img  # Keep reference
                        forecast_icon_label.pack()

                        # Temperature
                        tk.Label(card, text=f"{round(temp)}°F", bg=FORECAST_BG, fg=FORECAST_TEXT,
                                 font=(FONT_NAME, 12, "bold")).pack()

                        # Description
                        tk.Label(card, text=desc.title(), bg=FORECAST_BG, fg=FORECAST_TEXT,
                                 font=(FONT_NAME, 9)).pack()
                        break

    except Exception as e:
        print(f"Forecast error: {e}")
        result_label.config(text=f"Forecast error: {str(e)}", foreground="#FF0000")

# ===== CORE SETUP =====

# Main Window
app = tk.Tk()
app.title("Pink Weather App")
load_app_icon()  # This will try all possible ways to load your icon
app.geometry("600x500")

# Pink Gradiant Set Up
def create_gradient(width: int,
                   height: int,
                   color1: str = "#FFB6C1",
                   color2: str = "#FF69B4"):
    """
    Creates a vertical gradient and returns a PhotoImage
    Returns:
        ImageTk.PhotoImage: Tkinter-compatible image
    """
    # Create PIL Image
    pil_img = Image.new("RGB", (width, height))

    # Calculate gradient (keep your existing pixel calculation code)
    for y in range(height):
        r = int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * y // height
        g = int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * y // height
        b = int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * y // height

        for x in range(width):
            pil_img.putpixel((x, y), (r, g, b))

    # Return the PhotoImage
    return ImageTk.PhotoImage(pil_img)


# Create Gradient Background
gradient = create_gradient(600, 500, "#FFD1DC", "#FF69B4")

bg_label = tk.Label(app, image=gradient)  # type: ignore
bg_label._gradient = gradient
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create Animation Canvas
# noinspection PyArgumentList
canvas = tk.Canvas(app, bg='#FFD1DC', highlightthickness=0)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Make sure canvas stays behind other widgets
# noinspection PyArgumentList
canvas.lower("all")  # Sends canvas to background

# Weather Animations
class WeatherAnimation:
    def __init__(self, animation_canvas, effect_type):
        self.canvas = animation_canvas
        self.effect = WEATHER_EFFECTS[effect_type]
        self.particles = []
        self.active = False

    def start(self):
        self.active = True
        self._animate()

    def stop(self):
        self.active = False

    def _animate(self):
        if not self.active:
            return

        # Create new particles
        if random.random() > 0.7:
            x = random.randint(0, self.canvas.winfo_width())
            self.particles.append({
                'id': self.canvas.create_text(
                    x, -10,
                    text=self.effect["symbol"],
                    fill=self.effect["color"],
                    font=("Arial", 16),
                    tags="weather"
                ),
                'x': x,
                'y': -10,
                'speed': random.uniform(self.effect["speed"], self.effect["speed"] + 1)
            })

        # Move existing particles
        for p in self.particles[:]:
            self.canvas.move(p['id'], 0, p['speed'])
            p['y'] += p['speed']

            if p['y'] > self.canvas.winfo_height():
                self.canvas.delete(p['id'])
                self.particles.remove(p)

        self.canvas.after(30, self._animate)

# ===== WIDGET CREATION =====

# Main container
main_frame = ttk.Frame(app, style="Card.TFrame")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Input Group Frame
input_frame = ttk.Frame(main_frame)
input_frame.grid(row=0, column=0, columnspan=2, pady=10)

# City Label
ttk.Label(input_frame, text="Enter City:").pack(side="left", padx=(0, 5))

# City Entry with visible border
city_entry = ttk.Entry(
    input_frame,
    font=(FONT_NAME, 12),
    width=20,
    style="TEntry"  # Apply our new style
)
city_entry.pack(side="left")

# Results
result_label = ttk.Label(main_frame, font=(FONT_NAME, 14, "bold"), justify="center")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Weather Icon
icon_label = ttk.Label(main_frame)
icon_label.grid(row=1, column=0, columnspan=2, pady=10)

# Button
weather_btn = ttk.Button(
    main_frame,
    text="⛅ Get Weather",  # Added weather icon emoji
    command=fetch_weather,
    style="TButton"
)
weather_btn.grid(row=3, column=0, columnspan=2, pady=15, padx=15)  # Increased padding

# Add hover effects
def on_enter(_event):
    weather_btn.config(style="Hover.TButton")

def on_leave(_event):
    weather_btn.config(style="TButton")

weather_btn.bind("<Enter>", on_enter)
weather_btn.bind("<Leave>", on_leave)

# Forecast Title
tk.Label(
    main_frame,
    text="5-Day Forecast",
    bg=PINK_BG,
    fg=PINK_TEXT,
    font=(FONT_NAME, 14, "bold")
).grid(row=4, column=0, columnspan=2, pady=(20, 5))  # Adjust row number as needed

# Forecast Card Container
forecast_frame = tk.Frame(
    main_frame,
    bg=PINK_BG,
    padx=5,
    pady=5
)

forecast_frame.grid(row=5, column=0, columnspan=2)  # Place below other widgets

# Make widgets transparent by matching gradient colors
style = ttk.Style()
style.configure("TFrame", background=transparent)
style.configure("TLabel", background=transparent, foreground=PINK_TEXT, font=(FONT_NAME, 12))
style.configure("TButton", background=PINK_BTN, foreground="#5E2D50", font=(FONT_NAME, 12, "bold"), borderwidth=3, relief="raised", padding=10)
style.configure("Card.TFrame", background=transparent, borderwidth=2, relief="groove", padding=10)
style.configure("TEntry", foreground="#333333", fieldbackground="white", bordercolor="#FF69B4", padding=5, relief="solid", borderwidth=2)

# Add hover style
style.map("Hover.TButton", background=[("active", "#FF85C8")],  foreground=[("active", "white")],  relief=[("active", "sunken")])
style.map("Hover.TButton",  background=[("active", "#FF85C8")],  foreground=[("active", "white")],  relief=[("active", "sunken")])


# Add a subtle shadow effect to widgets
for widget in main_frame.winfo_children():
    # For ttk widgets
    if isinstance(widget, ttk.Widget):
        widget.configure(style='TLabel')
    # For regular tk widgets
    else:
        widget.configure(relief='flat', borderwidth=0)
    widget.grid_configure(padx=10, pady=5)

# Create the clock label (place at bottom of window)
clock_label = tk.Label(
    app,  # Note: Using 'app' instead of 'root' to match your code
    font=(FONT_NAME, 12),
    bg=PINK_BG,  # Matches your theme
    fg=PINK_TEXT,
    bd=0
)
clock_label.pack(side="bottom", pady=10)

# ===== INITIALIZATION =====
# Initialize animations
animations = {
    "snow": WeatherAnimation(canvas, "snow"),
    "rain": WeatherAnimation(canvas, "rain"),
    "clouds": WeatherAnimation(canvas, "clouds")
}

# ===== START APP =====
update_clock()  # Begin clock updates
app.mainloop()