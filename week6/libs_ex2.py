import requests

# Take input from user for name
name_input = input('Enter the name you want to search: ')

# Make the API request
response = requests.get(f"https://api.agify.io/?name={ name_input }")

# Parse JSON response
if response.status_code == 200:
    data = response.json()
    print(data)
    name = data.get("name", "Unknown")
    age = data.get("age", "Unknown")
    print(f"Name: {name}")
    print(f"Predicted Age: {age}")
else:
    print("Failed to retrieve data from API.")
