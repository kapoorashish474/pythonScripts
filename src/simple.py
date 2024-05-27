import os
import sys
import requests

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception if the status code is not 200
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/todos/2"
    result = fetch_data(api_url)
    if result:
        print(result)
    else:
        print("Error fetching data.")
    publisher_id = os.environ.get("PUBLISHER_ID")
    dev_token = os.getenv("DevToken")
    username = os.getenv("Username")
    password = os.environ.get("Password")
    print(publisher_id)
    print(dev_token)
    print(username)
    print(password)
    parameter = sys.argv[1]  # Access the passed parameter
    print(f"Received parameter: {parameter}")
