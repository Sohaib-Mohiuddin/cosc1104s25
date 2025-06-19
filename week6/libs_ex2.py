import requests

# Make the API request
response = requests.get("https://api.agify.io/?name=alex")

# Parse JSON response
if response.status_code == 200:
    data = response.json()
    name = data.get("name", "Unknown")
    age = data.get("age", "Unknown")
    print(f"Name: {name}")
    print(f"Predicted Age: {age}")
else:
    print("Failed to retrieve data from API.")
