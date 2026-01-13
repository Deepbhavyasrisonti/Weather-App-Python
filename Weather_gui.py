import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    unit = unit_var.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": unit
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        temp_unit = "°C" if unit == "metric" else "°F"

        weather_info = (
            f"City: {data['name']}\n"
            f"Temperature: {data['main']['temp']}{temp_unit}\n"
            f"Condition: {data['weather'][0]['description'].title()}\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Wind Speed: {data['wind']['speed']} m/s"
        )

        result_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "City not found")

def clear_data():
    city_entry.delete(0, tk.END)
    result_label.config(text="")
    city_entry.insert(0, "Hyderabad")

# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("Weather App")
root.geometry("420x360")
root.configure(bg="#e6f2ff")

# ---------------- VARIABLES ----------------
unit_var = tk.StringVar(value="metric")

# ---------------- UI ELEMENTS ----------------
tk.Label(root, text="Enter City Name", font=("Arial", 14, "bold"),
         bg="#e6f2ff").pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)
city_entry.insert(0, "Hyderabad")   # Default city

# Unit selection
frame_units = tk.Frame(root, bg="#e6f2ff")
frame_units.pack()

tk.Radiobutton(frame_units, text="°C", variable=unit_var, value="metric",
               bg="#e6f2ff").pack(side="left", padx=10)

tk.Radiobutton(frame_units, text="°F", variable=unit_var, value="imperial",
               bg="#e6f2ff").pack(side="left")

# Buttons
tk.Button(root, text="Get Weather", font=("Arial", 12),
          command=get_weather).pack(pady=8)

tk.Button(root, text="Clear", font=("Arial", 12),
          command=clear_data).pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12),
                        justify="left", bg="#e6f2ff")
result_label.pack(pady=10)

root.mainloop()
