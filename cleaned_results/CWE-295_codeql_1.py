import requests

try:
    response = requests.get("https://semmle.com")
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    print("Status Code:", response.status_code)
    print("Content:", response.text)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)