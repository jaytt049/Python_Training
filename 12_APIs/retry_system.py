import requests
import time

url = "https://jsonplaceholder.typicode.com/posts/1"

retries = 3

for i in range(retries):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print("success : ", response.json())
            break
        else:
            print("failed to attempt ", i+1)
    except requests.exceptions.RequestException:
        print("Error Occured, retrying", i+1)
    
    time.sleep(2)
else:
    print("all retries are failed.")
