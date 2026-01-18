import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *

cfg = config()
base = cfg['API']['base_url']
url = f"{base}{apiRessources.searchProduct}"

data = {"search_product": "tshirt"}

def test_post_search_product():
    with allure.step('produit recherché'):
        response = requests.post(url, data=data)

        assert response.status_code == 200

        response_body = response.json()
        print_json(data=response_body)

        allure.attach(str(response.status_code), 'Code HTTP')
        allure.attach(response.text, 'response API')