import requests
from bs4 import BeautifulSoup

url = "https://softech.kg/phones/apple-smartphone/"

iphone = requests.get(url)

soup = BeautifulSoup(iphone.text, 'html.parser')

product_box = soup.find_all('div', class_ = 'caption')

for product in product_box:
    name = product.find(class_ = 'name')
    price = product.find(class_ = 'price')
    print(name.text)
    print(price.text)

