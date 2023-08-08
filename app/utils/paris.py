import httpx
from bs4 import BeautifulSoup

def get_product_data(url: str, client: httpx.Client | None = None):
    # url = https://www.paris.cl/consola-ps5-con-disco-juego-fifa-2023-116963999.html

    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find("div", {"class": "price__inner"})
    prices = div.find_all("div", {"class":"price__text" }) # card-price internet-price
    normal_price = div.find("div", {"class":"price__text-sm" }).string.replace('\n', '').replace('$','')

    product = {
        "normal-price": normal_price.replace('$',''),
        "event-price": "",
        "internet-price": "",
        "card-price": "",
    }

    if len(prices) > 1:
        product["internet-price"] = prices[1].string.replace("\n", "").replace('$','')
        product["card-price"] = prices[0].string.replace("\n", "").replace('$','')
    else:
        product["internet-price"] = prices[0].string.replace("\n", "").replace('$','')

    if product["normal-price"] == "":
        product["normal-price"] = product["internet-price"]

    name = soup.find("h1", {"class": "js-product-name"}).string.replace('\n','')
    product["name"] = name

    return product