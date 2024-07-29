import requests
import json

# URL of the API
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Save the JSON response to a file
    with open('raw_data/stock_data.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("Data saved to stock_data.json")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
