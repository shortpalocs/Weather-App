import customtkinter as ctk
import requests
import os
API_KEY = r"Enter your own! Can't share API Keys sorry."

ctk.set_appearance_mode("dark")
from dotenv import load_dotenv




def getweather():
    global weatheremoji
    cityname = weatherentry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()




    if data["cod"] != 200:
        weather_label.configure(text="City not found or invalid input.")
        showemoji.configure(text="❌")
        return

    if data["cod"] == 200:
        city = data["name"]
        print("")
        pressure = data["main"]["pressure"]
        temp = data["main"]["temp"]
        weatherdesc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_info = f"City: {city}\nTemperature: {temp}°C\nWeather: {weatherdesc.capitalize()}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s \nPressure: {pressure} hPa"
        weather_label.configure(text=weather_info)


        weatheremojis = {"clear sky": "☀️",
        "few clouds": "⛅",
        "scattered clouds": "🌥️",
        "broken clouds": "☁️",
        "shower rain": "🌧️",
        "rain": "🌦️",
        "thunderstorm": "⛈️",
        "snow": "❄️",
        "mist": "🌫️"}




        weatheremoji = weatheremojis.get(weatherdesc.lower(), "🌎")
        showemoji.configure(text=weatheremoji)









root = ctk.CTk()
root.geometry("600x400")
root.title("Weather App")



weatherentry = ctk.CTkEntry(root, placeholder_text="      Enter city name ")
weatherentry.place(x=240, y=50)


weather_label = ctk.CTkLabel(root, text="WEATHER APPEARS HERE", font=("Arial", 14))
weather_label.place(x=225, y=80)


button = ctk.CTkButton(root, text="Get Weather", command=getweather)
button.place(x=240, y=250)
showemoji = ctk.CTkLabel(root, text="🌎", font=("Arial", 60))
showemoji.place(x=270, y=285)


root.mainloop()