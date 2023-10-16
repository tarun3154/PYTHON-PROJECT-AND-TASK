import requests
API_KEYS = "313d651b3b814588b363aa1998f24309"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


City = input("Enter your city")

request_url = f"{BASE_URL}?appid={API_KEYS}&q={City}"
response = requests.get(request_url)


if response.status_code == 200:
    data= response.json()
    print(data)

else:
    print("Got a error")