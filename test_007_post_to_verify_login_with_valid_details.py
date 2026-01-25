import allure
from rich import print_json
import requests
from utilities.configuration import *
from utilities.ressources import *


cfg = config()
base_url = cfg['API']['base_url']
url = f"{base_url}{apiRessources.loginValid}"
params = {
            "email": "elodielacombe@example.com",
            "password": "#)XM4$SxaY"
}

def test_post_to_verify_login_with_valid_details():
    with allure.step('test valid login'):
        response = requests.post(url, data=params)

        assert response.status_code == 200

        response_body = response.json()
        print_json(data=response_body)

        assert response_body["responseCode"] == 200
        assert response_body["message"] == "User exists!"

        allure.attach(response.text, "response API")
        allure.attach(str(response.status_code), "Code HTTP")
