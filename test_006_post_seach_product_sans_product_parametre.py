import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *

cfg = config()
base = cfg['API']['base_url']
url = f"{base}{apiRessources.searchProduct}"


def test_post_search_product_without_info_product():
    with allure.step('produit recherché sans renseigner produit'):
        response = requests.post(url)

        assert response.status_code == 200

        response_body = response.json()
        print_json(data=response_body)

        assert response_body["responseCode"] == 400

        allure.attach(str(response.status_code), 'Code HTTP')
        allure.attach(response.text, 'response API')