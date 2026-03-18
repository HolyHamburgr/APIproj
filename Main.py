# @author = Aldrin Torres
# @class = AP CSA "Learning API with Python!"
# Class of 2025

import requests # this library is not available in codeHS
import sys

def get_flights(access_key, dep_iata, arr_iata):
    """Fetch flight data from Aviationstack API.
	https://aviationstack.com/ for singup and documentation
	"""
	
    
    # Only realtime data works with the free tier (no flight_date param)
    api_url = (
        f"http://api.aviationstack.com/v1/flights"
        f"?access_key={access_key}"
        f"&dep_iata={dep_iata}"
        f"&arr_iata={arr_iata}"
    )

    response = requests.get(api_url)
    response.raise_for_status()  # Raises error for bad status codes (like 403)
    return response.json()


def display_flights(data):
    """Parse and display flight information."""
    
    flights = data.get("data", [])

    if not flights:
        print("No flights found for the selected route.")
        return

    for i, flight in enumerate(flights, start=1):
        airline      = flight.get("airline", {}).get("name", "Unknown")
        departure    = flight.get("departure", {})
        arrival      = flight.get("arrival", {})
        
        dep_airport  = departure.get("airport", "Unknown")
        dep_time     = departure.get("scheduled", "N/A")
        arr_airport  = arrival.get("airport", "Unknown")
        arr_time     = arrival.get("scheduled", "N/A")
        status       = flight.get("flight_status", "N/A")

        print(f"Flight {i}")
        print(f"  Airline:           {airline}")
        print(f"  Departure Airport: {dep_airport}")
        print(f"  Departure Time:    {dep_time}")
        print(f"  Arrival Airport:   {arr_airport}")
        print(f"  Arrival Time:      {arr_time}")
        print(f"  Status:            {status}")
        print("  ---------------------------")


def main():
    print(f"Python version: {sys.version}")

    # --- Configuration ---
    ACCESS_KEY = "201dab8355861580f3cc6c15fc7e4230"  # Replace with your key
    DEP_IATA   = "JFK"  # Departure airport code
    ARR_IATA   = "MCO"  # Arrival airport code

    try:
        data = get_flights(ACCESS_KEY, DEP_IATA, ARR_IATA)
        display_flights(data)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet connection.")
    except Exception as e:
        print(f"Error: {e}")


# Python starts the program here.
# It says: "If you're running THIS file (not importing it), then run main()."

if __name__ == "__main__":
    main()
'''
# further development ideas: AP CSP 2027
# - Add user input for airport codes and date
# - Handle pagination if there are many flights 

---

### `requirements.txt`
```'''
#requests==2.31.0