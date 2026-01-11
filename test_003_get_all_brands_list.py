import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *


config = config()
base = config['API']['base_url']
url = f"{base}{apiRessources.brandList}"


def test_get_all_brands():
    with allure.step("Get all brands"):
        response = requests.get(url)

        assert response.status_code == 200

        allure.attach(str(response.status_code), "Code HTTP")
        allure.attach(response.text, "RESPONSE API")

        body = response.json()
        print_json(data=body)