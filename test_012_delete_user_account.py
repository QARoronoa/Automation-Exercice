import allure
import requests
from rich import print_json
from utilities.configuration import *
from utilities.ressources import *


cfg = config()
base_url = cfg['API']['base_url']
url = f"{base_url}{apiRessources.deleteAccount}"
params = {"email" : "hamiltonjoseph@example.com", "password" : "azerty"}


with allure.step('delete user account'):
    def test_delete_user_account():
        response = requests.delete(url, data=params)

        allure.attach(str(response.status_code), "code http")
        allure.attach(response.text, 'Response API')

        response_body = response.json()
        print_json(data=response_body)

        assert response.status_code == 200
        assert response_body["message"] ==  "Account deleted!"
