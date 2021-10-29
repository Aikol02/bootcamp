import requests
    
def main():
    novosti_url = 'https://vesti.kg/itemlist.html?start=0'
    html = get_html(novosti_url)

main()