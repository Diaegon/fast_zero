from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_hello_world():
    client = TestClient(app) #arrange
    response = client.get('/')#act
    assert response.status_code == HTTPStatus.OK  #assert
    assert response.json() == {'message': 'hello world'}#assert
