import requests

API_KEY = "b4ee546aeaf7eff0e3de235b777e4754"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    wind = data["wind"]["speed"]
    
    print("weather:", weather)
    print("Temerature: ", temperature, "Celsius")
    print("wind: ", wind, "ms")
else:
    print("error occurred")
