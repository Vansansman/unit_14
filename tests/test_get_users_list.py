import logging
import requests
from pytest_voluptuous import S
from schemas.user import users_list_schema


def test_get_user_list_schema():
    result = requests.get("https://reqres.in/api/users", params={"page": 2})
    logging.info(result.json())

    assert S(users_list_schema) == result.json()

def test_users_count_on_page():
    """проверка, что на странице 6 пользователей"""

    responses = requests.get("https://reqres.in/api/users", params={"page": 1})
    per_page = responses.json()["per_page"]
    data = responses.json()["data"]

    assert  per_page == 6
    assert len(data) != 9

def test_post_user():
    url = 'https://reqres.in/api/users'
    data = {'name': 'Margaret', 'age': '40'}
    response = requests.post(url, data=data)

    assert response.status_code == 201
    assert response.json()['name'] == 'Margaret'
    assert response.json()['age'] == '40'




