import requests
import json

# URL of the API
base_url = 'https://www.alphavantage.co'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo'



def get_daily_data(stock, outputsize='full',apikey='demo'):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&outputsize={outputsize}&apikey={apikey}'
    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Save the JSON response to a file
        file_name = f'raw_data/stock_daily_{stock}.json'
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

        print("Data saved to:"+file_name)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)


def get_weekly_data(stock, apikey='demo'):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={stock}&apikey={apikey}'
    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Save the JSON response to a file
        file_name = f'raw_data/stock_weekly_{stock}.json'
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

        print("Data saved to:"+file_name)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)


def get_monthly_data(stock, outputsize='full',apikey='demo'):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={stock}&apikey={apikey}'
    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Save the JSON response to a file
        file_name = f'raw_data/stock_monthly_{stock}.json'
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

        print("Data saved to:"+file_name)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

if __name__ == "__main__":
    # get_daily_data(stock='TSCO.LON')
    # get_weekly_data(stock='TSCO.LON')
    get_monthly_data(stock='TSCO.LON')