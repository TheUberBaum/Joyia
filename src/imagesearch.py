from requests_html import HTMLSession

import requests
from bs4 import BeautifulSoup
search_term = 'flower'
url = rf'https://www.google.no/search?q={search_term}&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&safe=active&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

thumbnails = []
for raw_img in soup.find_all('img'):
    link = raw_img.get('src')
    if link and link.startswith("https://"):
        thumbnails.append(link)
        pass
    pass

session = HTMLSession()
url = 'https://www.google.pl/search?q=python&source=lnms&tbm=isch&sa=X&ved=0ahUKEwif6Zq7i8vaAhVMLVAKHUDkDa4Q_AUICigB&biw=1280&bih=681'
url = 'https://www.google.com/search?q=python&tbm=isch&sclient=img'
r = session.get(url)
r.html.render()

first_image = r.html.find('.rg_ic.rg_i', first=True)
print(first_image)

link = first_image.attrs['src']
print(link)
