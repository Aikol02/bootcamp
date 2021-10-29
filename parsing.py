from bs4 import BeautifulSoup
import requests 
 

def get_html(url):
    responce = requests.get(url)
    print(responce.status_code)



def main():
    nootbooks_url = 'https://www.eldorado.ru/c/noutbuki/tag/macbook-air/'
    pages = '?page='