from bs4 import BeautifulSoup
import requests



page = requests.get('https://indeks.kompas.com/headline')
soup = BeautifulSoup(page.text, 'html.parser')

if page.status_code == 200: div = soup.find_all(class_= "article__link")
title = [t.text for t in div]
url = [u['href'] for u in div]
for i in range(len(title)):
    res = list({url[i], title[i]})
    print("Title :",res[1], "\n" "URL :",res[0])