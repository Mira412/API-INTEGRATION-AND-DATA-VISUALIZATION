import requests
import matplotlib.pyplot as plt

API_KEY = 'd461d57a0ba725488be6a5980c228ae4'
CITY = 'Mumbai'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)
data = response.json()

temp = data['main']['temp']
humidity = data['main']['humidity']

plt.figure(figsize=(5, 5))
plt.bar(['Temperature (°C)', 'Humidity (%)'], [temp, humidity], color=['blue', 'green'])
plt.title(f'Weather Data for {CITY}')
plt.show()
