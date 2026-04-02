# Free API (JSONPlaceholder)

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Failed to fetch data")

# Key Concepts
# requests.get() → send request
# status_code → check success (200 = OK)
# .json() → convert response to Python dict

import requests

url = "https://bmsmart-backend-deploy.onrender.com/visitors/building/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("something went wrong.")