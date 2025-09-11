from http import HTTPStatus

from fast_zero.schemas import UserPublic

"""def test_root_deve_retornar_hello_world(client):
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'hello world'}  # assert


def test_ola_deve_retornar_html(client):
    response = client.get('/ola')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert '<h1>Olá, Mundo!</h1>' in response.text  # assert
"""


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'diego',
            'email': 'diego@exemple.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'diego',
        'email': 'diego@exemple.com',
        'id': 1,
    }


def test_create_user_integrity_error_user(client, user):
    response = client.post(
        'users/',
        json={
            'username': 'Teste',
            'email': 'test@test.com',
            'password': 'passwordzinho',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username already exists'}


def test_create_user_integrity_error_email(client, user):
    response = client.post(
        'users/',
        json={
            'username': 'Teste2',
            'email': 'teste@test.com',
            'password': 'passwordzinho',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email already exists'}


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_read_user_with_id(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(f'/users/{user.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bobexemple@gmail.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bobexemple@gmail.com',
        'id': 1,
    }


def test_update_integrity_error(client, user):
    client.post(
        '/users',
        json={
            'username': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )

    response_update = client.put(
        f'/users/{user.id}',
        json={
            'username': 'fausto',
            'email': 'bobexemple@gmail.com',
            'password': 'mynewpassword',
        },
    )
    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {
        'detail': 'Username or Email already exists'
    }


def test_read_user_id_not_found(client, user):
    response = client.get(f'/users/{user.id + 13}')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_not_found(client, user):
    response = client.put(
        f'/users/{user.id + 13}',
        json={
            'username': 'bob marley',
            'email': 'bob2@gmail.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete(f'/users/{user.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client, user):
    response = client.delete(f'/users/{user.id + 13}')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found',
    }
