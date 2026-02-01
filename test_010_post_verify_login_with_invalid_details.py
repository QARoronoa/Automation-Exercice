import allure
from rich import print_json
from utilities.configuration import *
from utilities.ressources import *
import requests

cfg = config()
base_url = cfg['API']['base_url']
url = f"{base_url}{apiRessources.loginValid}"
params = {
    "email" : "jkjkj@ms.com",
    "password" : "fldfkldkf"
}

with allure.step('login with invalid details'):
    def test_login_with_invalid_details():
        response = requests.post(url, json=params)

        allure.attach(response.text, 'API response')
        allure.attach(str(response.status_code), 'CODE HTTP')

        response_body = response.json()
        print_json(data=response_body)

        assert response.status_code == 200
        assert response_body["responseCode"] == 400