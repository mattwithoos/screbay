import requests
from bs4 import BeautifulSoup
#price_limit = str(input('Max price (only numbers, default 3000): ') or '3000')
price_limit = "2400"
URL = 'https://www.ebay.com.au/sch/i.html?_from=R40&_nkw=rtx+3080&_sacat=0&LH_TitleDesc=0&_sop=15&_udlo=1000&_udhi='+price_limit+'&rt=nc&LH_BIN=1&LH_PrefLoc=1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

gpus = soup.find_all('li', class_='s-item')

count = 0;
print('Results:\n')
print('------------------------\n')
for gpu in gpus:
    title = gpu.find('h3', class_='s-item__title')
    price = gpu.find('span', class_='s-item__price')
    location = gpu.find('span', class_='s-item__location s-item__itemLocation')
    link = gpu.find('a', class_='s-item__link')
    if None in (title, price):
        continue

    # some dodgy sellers include words like below to appear in listings...
    filteredCards = ['2080','3070','3060']
    shouldFilter = [(x in title.text) for x in filteredCards]
    if True in shouldFilter:
        continue

    # ebay loves showing international results...
    if location != None:
        continue

    print(title.text.strip())
    print(price.text.strip())
    print(link['href'].strip())
    count = count + 1;

print('------------------------\n')
print(f'Finished! Found {count}')