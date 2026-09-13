import requests

API_KEY = "af830252df7f2c873a7d50ca4e795745"

def get_data(place, forecast_days=None, displaying_way=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
   print(get_data(place="Tokyo"))