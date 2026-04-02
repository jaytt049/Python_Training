import requests

api_key = "abfacd7d36b59fdec89c22221945aec7"
city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

print(response.status_code)
print(response.text)

if response.status_code == 200:
    data = response.json()
    print("Temperature:", data["main"]["temp"])
    print("Weather:", data["weather"][0]["description"])
else:
    print("City not found or API error")