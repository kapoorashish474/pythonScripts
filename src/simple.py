import requests

# Specify the URL of the API endpoint you want to access
api_url = "https://jsonplaceholder.typicode.com/todos/1"

# Send a GET request
response = requests.get(api_url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
