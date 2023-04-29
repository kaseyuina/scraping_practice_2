import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/ranking'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
stops = soup.find_all('div', attrs={'class': 'u_areaListRankingBox'})
stop = stops[0]