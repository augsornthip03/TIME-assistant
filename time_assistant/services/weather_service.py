import requests

def get_weather(city,api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    api_url = f"{base_url}?key={api_key}&q={city}&aqi=no"
    response = requests.get(api_url)
    try:
        response.raise_for_status()
        data = response.json()
        info = {
            'city' : data["location"]['name'],
            'temp_c' : data['current']['temp_c'],
            'condition' : data['current']['condition']['text']
        }
        return info
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the API: {e}")
        return None
    





