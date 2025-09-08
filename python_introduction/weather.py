import requests

weath_info = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY")
print(weath_info.json())