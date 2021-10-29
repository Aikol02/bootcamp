import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    return response.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages_i = soup.find('div', class_='seb-pagination__pages').find('i')


def main():
    noutbooks_url = 'https://www.alibaba.com/products/noutbook.html?IndexArea=product_en&'
    pages = '?page='
    get_total_pages(get_html(noutbooks_url))

main()