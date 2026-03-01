import allure

from utilities.ressources import *
from utilities.configuration import *
from rich import print_json
import requests


cfg = config()
base = cfg['API']['base_url']
url = f'{base}{apiRessources.userdetailAccount}'
params = {"email" : "dferguson@example.org"}

with allure.step('get user details account'):
    def test_get_user_details_account():
        response = requests.get(url, params=params)

        allure.attach(str(response.status_code), 'CODE HTTP')
        allure.attach(response.text, 'response API')

        response_body = response.json()
        print_json(data=response_body)

        assert response.status_code == 200

