import requests
from pytest_voluptuous import S
from requests import Response
from voluptuous import Schema, PREVENT_EXTRA
from  schemas.user import single_user_schema

def test_get_users():
    response: Response = requests.get("https://reqres.in/api/users/2",)
    print(response.status_code)


    assert response.status_code == 200
    assert response.json()["data"]["email"] =="janet.weaver@reqres.in"

def test_get_users_avatar_filed():
    response: Response = requests.get("https://reqres.in/api/users/2",)
    print(response.status_code)

    assert response.status_code == 200
    assert response.json().get("data").get("avatar", None)

def test_get_users_has_avatar_exists():
    response: Response = requests.get("https://reqres.in/api/users/2", )
    print(response.status_code)
    avatar = response.json().get("data").get("avatar")
    result = requests.get(avatar)

    assert result.status_code == 200
    assert len(response.content) !=0
    assert len(response.content) == 280


def test_get_users_schema():
    response = requests.get("https://reqres.in/api/users/2")

    assert response.status_code == 200
    assert S(single_user_schema) == response.json()





