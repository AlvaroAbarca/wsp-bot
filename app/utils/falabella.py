import httpx
from bs4 import BeautifulSoup

def get_product_data(url: str, client: httpx.Client | None = None):
    # url = "https://www.falabella.com/falabella-cl/product/16739166/Consola-Playstation-5-Standard/16739166"

    id = [x for x in url.split("/") if x.isdigit()][0]
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find("div", {"class": "price"})

    product = {
        "normal-price": 0,
        "event-price": 0,
        "internet-price": 0,
        "card-price": 0
    }

    for li in div.ol.contents:
        if "data-normal-price" in li.attrs.keys():
            product["normal-price"] = li.attrs["data-normal-price"]
        elif "data-event-price" in li.attrs.keys():
            product["event-price"] = li.attrs["data-event-price"]
        elif "data-internet-price" in li.attrs.keys():
            product["internet-price"] = li.attrs["data-internet-price"]
        elif "data-cmr-price" in li.attrs.keys():
            product["card-price"] = li.attrs["data-cmr-price"]

    if product["normal-price"] == "":
        product["normal-price"] = product["internet-price"]

    name = soup.find("div", {"class": "fa--product-name"})
    image = "https://falabella.scene7.com/is/image/Falabella/{}".format(id)
    product["name"] = name.attrs["data-name"]
    product["image"] = image

    return product