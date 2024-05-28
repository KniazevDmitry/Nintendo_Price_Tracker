from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.nintendo.com/us/store/products/minecraft-switch/'
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')

    script_tag = soup.find('script', type="application/ld+json")
    json_data = script_tag.string
    data = json.loads(json_data)

    game_name = data['name']
    game_price = data['offers']['price']
    game_currency = data['offers']['priceCurrency']

    print(game_name)
    print(f"{game_price} {game_currency}")
else:
    print(f"Error: {response.status_code}")