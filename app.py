from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API Key (Directly Used)
API_KEY = "665992eb3e130d58370b20a2b03d4e9f"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].capitalize(),
                "icon": f"http://openweathermap.org/img/w/{data['weather'][0]['icon']}.png",
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
            }
        else:
            weather_data = {"error": "City not found! Please try again."}
    
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
