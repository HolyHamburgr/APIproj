import requests
import sys

# base = "https://pokeapi.co/api/v2/"

# def get_poke_info(name):
#  url = f"{base}/pokemon/{name}"
#  response = requests.get(url)
#  if response.status_code == 200:
#   print("Success!")
#   data = response.json()
#   return data
#  else:
#   print(f"Failure{response.status_code}")

# poke_name = "diglett"
# poke_info = get_poke_info(poke_name)

# if poke_info:
#  print(f"{poke_info["name"]}")
#  print(f"{poke_info["id"]}")

base = "https://rickandmortyapi.com/api/"

def get_char_info(id):
    url = f"{base}character/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        
        data = response.json()
        return data
    else:
        print(f"Failure{response.status_code}")


id = input("ID code between 1 and 826: ")
# for char in id:
#     try:
        
#         int(char)

#         api_info = get_char_info(char)
#         if api_info:
#             print(f"Name: {api_info['name']}")
#             print(f"Status: {api_info['status']}")
#             print(f"Species: {api_info['species']}")
#             print(f"Gender: {api_info['gender']}")
#             print("-----------------------------------------")

#     except ValueError:
#         print(f"Skipping invalid ID: {char}")
#     except requests.exceptions.HTTPError as e:
#         print(f"HTTP Error: {e}")
#     except requests.exceptions.ConnectionError:
#         print("Error: Could not connect to the API. Check your internet connection.")
#     except Exception as e:
#         print(f"Error: {e}")

# for char in id:
#     if int(char):
#     try:
#         api_info = get_char_info(char)
#         if api_info:
#             print(f"Name: {api_info['name']}")
#             print(f"Status: {api_info['status']}")
#             print(f"Species: {api_info['species']}")
#             print(f"Gender: {api_info['gender']}")
#             print("-----------------------------------------")

#     except requests.exceptions.HTTPError as e:
#         print(f"HTTP Error: {e}")
#     except requests.exceptions.ConnectionError:
#         print("Error: Could not connect to the API. Check your internet connection.")
#     except Exception as e:
#         print(f"Error: {e}")
# for char in id:
      
try:
    api_info = get_char_info(id)
    if api_info:
        print(f"Name: {api_info["name"]}")
        print(f"Status: {api_info["status"]}")
        print(f"Species: {api_info["species"]}")
        print(f"Gender: {api_info["gender"]}")
        print("-----------------------------------------")
        
except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet connection.")
except Exception as e:
        print(f"Error: {e}")
