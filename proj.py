import requests
import sys

url = 'https://rickandmortyapi.com/api'
def get_characters():
    """Fetch flight data from Aviationstack API.
	https://aviationstack.com/ for singup and documentation
	"""
	
    
    # Only realtime data works with the free tier (no flight_date param)
    api_url = (
        f"https://rickandmortyapi.com/api/character"
    )

    response = requests.get(api_url)
    return response.json()

def display_characters(data):
    """Parse and display flight information."""
    
    characters = data.get("data", [])


    for i, char in enumerate(characters, start=1):
        
        status       = char.get("flight_status", "N/A")
        name = char.get("name")
        print(f" Name:       {name}")



def main():
    print(f"Python version: {sys.version}")

    try:
        data = get_characters()
        display_characters(data)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet connection.")
    except Exception as e:
        print(f"Error: {e}")