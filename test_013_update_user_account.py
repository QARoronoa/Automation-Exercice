import allure
import requests
from utilities.ressources import *
from utilities.configuration import *
from rich import print_json

cfg = config()
base_url = cfg['API']['base_url']
url = f"{base_url}{apiRessources.updateAccount}"
data = {"name" : "looioi",
         "email" : "hansonandrew@example.org",
         "password" : "azerty",
         "title" : "Mr",
         "firstname" : "sfsf",
         "lastname": "ooooo",
         "address1" : "sdsdsd",
         "country" : "france",
         "zipcode" : 92350,
         "state" : "cfl",
         "city" : "ee",
         "mobile_number" : 3333333}

with allure.step('update an account'):
    def test_update_account():
        response = requests.put(url, data=data)

        allure.attach(str(response.status_code), 'Code HTTP')
        allure.attach(response.text, 'response api')

        response_body = response.json()
        print_json(data=response_body)

        assert response.status_code == 200
        assert response_body["message"] == "User updated!"
