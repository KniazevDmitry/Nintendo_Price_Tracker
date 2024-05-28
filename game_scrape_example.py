from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.nintendo.com/us/store/products/minecraft-switch/'
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')

    script_tag = soup.find('script', type="application/ld+json")
    if script_tag:
        try:
            json_data = script_tag.string
            data = json.loads(json_data)

            game_name = data.get('name', 'N/A')
            game_price = data.get('offers', {}).get('price', 'N/A')
            game_currency = data.get('offers', {}).get('priceCurrency', 'N/A')

            print(game_name)
            print(f"{game_price} {game_currency}")
        except json.JSONDecodeError:
            print("Error parsing JSON data.")
    else:
        print("JSON-LD script tag not found.")
else:
    print(f"Error: {response.status_code}")