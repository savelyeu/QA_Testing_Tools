import requests
from bs4 import BeautifulSoup

url = 'https://www.animatsioon.com'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

title = soup.find('title').text
print('Title:', title)

