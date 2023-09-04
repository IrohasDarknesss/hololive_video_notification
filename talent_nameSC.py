from bs4 import BeautifulSoup as bs
import requests

source = 'https://hololive.hololivepro.com/talents'
req = requests.get(source)
req.encoding = req.apparent_encoding
soup = bs(req.text, 'html.parser')

href_list = []
div = soup.find_all('div', class_ = 'container')
for talent in div:
    _talent = talent.find_all('a')
    for a_tag in _talent:
        href_list.append(a_tag['href'])
print(href_list)

txt_path = './text/talents.txt'
with open(txt_path, 'w', encoding='utf-8') as f:
    for href in href_list:
        f.write(href + '\n')