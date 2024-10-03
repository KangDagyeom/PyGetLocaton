import requests

def get_location():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    return data

location = get_location()
print("Location:", location)

