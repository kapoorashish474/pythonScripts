import os
import requests

def get_data(api_url):
    """
    Fetches data from the specified API endpoint.

    Args:
        api_url (str): The URL of the API endpoint.

    Returns:
        dict: Parsed JSON data from the response.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception if the status code is not 200
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    custom_api = os.getenv("PUBLISHER_ID")
    print(custom_api)  
    custom_api = os.getenv("PUBLISHERID")
    print(customapi)  
    if not custom_api:
        custom_api = "https://jsonplaceholder.typicode.com/todos/2"  # Default URL

    result = get_data(custom_api)
    if result:
        print(result)
    else:
        print("Error fetching data.")
