from http import HTTPStatus


def test_root_deve_retornar_hello_world(client):
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'hello world'}  # assert


def test_ola_deve_retornar_html(client):
    response = client.get('/ola')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert '<h1>Olá, Mundo!</h1>' in response.text  # assert


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


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'diego',
                'email': 'diego@exemple.com',
                'id': 1,
            }
        ]
    }


def test_read_user_id(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'diego',
        'email': 'diego@exemple.com',
        'id': 1,
    }


def test_read_user_id_not_found(client):
    response = client.get('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_server(client):
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


def test_update_user_not_found(client):
    response = client.put(
        '/users/999',
        json={
            'username': 'bob marley',
            'email': 'bob2@gmail.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User deleted',
    }


def test_delete_user_not_found(client):
    response = client.delete('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found',
    }
