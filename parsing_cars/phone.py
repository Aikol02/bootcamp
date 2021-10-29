import requests
from bs4 import BeautifulSoup as BS

import csv

def get_html(url):
    responce = requests.get(url)
    return responce.text 

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_="list-view")
    phons = catalog.find_all('div', class_="item")
    for phone in phons:
        try:
            title = phone.find('div', class_="listbox_title").text.strip()
        except:
            title = 'A phone'

        try:
            img = phone.find('div', class_="listbox_img").find('img').get('src')
        except:
            img = 'https://www.kivano.kg/product/view/sotovyy-telefon-bravis-a552-joy-max-zolotoy'
        try:
            price = phone.find('div', class_="listbox_price").find('strong').text.strip()
        except:
            price = 'Договорная'

        data = {
            'title': title,
            'price': price,
            'img': img
        }

        write_to_csv(data)

def write_headers():
    with open('phons.csv', 'a') as file:
        fieldnames = ['Марка телефона', 'Стоимость', 'Фотография']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def write_to_csv(data):
    with open('phons.csv', 'a') as file:
        fieldnames = ['Марка телефона', 'Стоимость', 'Фотография']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Марка телефона': data['title'],
                          'Стоимость': data['price'],
                          'Фотография': data['img']})


def main():
    with open('phons.csv', 'w') as file:pass
    write_headers()
    i = 1
    while True:
        phone_url = f'https://www.kivano.kg/mobilnye-telefony?page={i}'
        html = get_html(phone_url)
        catalog = BS(html, 'lxml').find('div', class_="list-view")
        if not catalog:
            break
        get_data(html)
        i += 1

main()
