import allure
from rich import print_json
import requests
from utilities.ressources import *
from utilities.configuration import *

cfg = config()
base_url = cfg['API']['base_url']
url = f"{base_url}{apiRessources.productList}"


def test_get_all_products():
    with allure.step("get all products"):
        response = requests.get(url)

        assert response.status_code == 200

        response_body = response.json()
        print_json(data=response_body)

        allure.attach(str(response.status_code), "Code HTTP")
        allure.attach(response.text, "Api response")