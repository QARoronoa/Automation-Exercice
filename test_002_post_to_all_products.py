import allure
import requests
from rich import print_json
from utilities.configuration import *
from utilities.ressources import *

cfg =config()
base = cfg['API']['base_url']
url = f"{base}{apiRessources.productList}"

def test_post_to_all_product_list():
    with allure.step("Post products to all product"):
        response = requests.post(url)

        response_body = response.json()

        assert response.status_code == 200
        assert response_body["responseCode"] == 405
        assert response_body["message"] == "This request method is not supported."


        print_json(data=response_body)

        allure.attach(str(response.status_code), "Code HTTP")
        allure.attach(response.text, "Api response")