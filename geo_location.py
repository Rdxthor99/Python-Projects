import requests

def get_location():
    try:
        # Sending a request to ipinfo.io API
        response = requests.get('https://ipinfo.io/')
        data = response.json()

        # Extracting the required information
        loc = data['loc'].split(',')
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')

        # Printing the location and coordinates
        print(f"Latitude: {loc[0]}, Longitude: {loc[1]}")
        print(f"Location: {city}, {region}, {country}")
        
        return {
            "latitude": loc[0],
            "longitude": loc[1],
            "city": city,
            "region": region,
            "country": country
        }

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
location = get_location()
