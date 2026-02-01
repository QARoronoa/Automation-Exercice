import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *


cfg = config()
base_url = cfg['API']['base_url']
url = f"{base_url}{apiRessources.loginValid}"


def test_post_login_without_parameter():
    with allure.step('test login without email & password'):
        response = requests.post(url)

        assert response.status_code == 200

        response_body = response.json()
        print_json(data=response_body)

        assert response_body["responseCode"] == 400
        assert response_body["message"] == "Bad request, email or password parameter is missing in POST request."