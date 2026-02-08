import allure
from faker import Faker
from utilities.ressources import *
from utilities.configuration import *
from rich import print_json
import requests

faker = Faker()
cfg = config()
base = cfg['API']['base_url']
url = f"{base}{apiRessources.createAccount}"
param = {"name" : "looioi",
         "email" : faker.email(),
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

with allure.step('create account'):
    def test_post_create_account():
        response = requests.post(url, data=param)

        allure.attach(str(response.status_code), 'CODE HTTP')
        allure.attach(response.text, 'response API')

        response_body = response.json()
        print_json(data=response_body)
        print(param["email"])

        assert response.status_code == 200
        assert response_body["message"] == "User created!"
