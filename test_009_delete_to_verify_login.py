import allure
from rich import print_json
from utilities.configuration import *
from utilities.ressources import *
import requests

cfg = config()
base_url = cfg['API']['base_url']
url = f"{base_url}{apiRessources.loginValid}"

with allure.step('delete login'):
    def test_delete_to_verify_login():
        response = requests.delete(url)

        response_body = response.json()
        print_json(data=response_body)

        assert response.status_code == 200
        assert response_body["responseCode"] == 405

        allure.attach(str(response.status_code), "CODE HTTP")
        allure.attach(response.text, "Api response")