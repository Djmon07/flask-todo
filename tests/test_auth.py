import pytest

from flasktodo.db import get_db

def test_register(client, app):

    assert client.get('/register').status_code == 200

    response = client.post('/register', data={'username': 'user1', 'password': 'User1_123'})
    #A successful registration should redirect to the index
    assert response.headers['Location'] == 'http://localhost/'

    #Trying to register an already existing user should fail and return a message
    response = client.post('/register', data={'username': 'user1', 'password': 'User2_123'})

    assert b'user1 is already registered' in response.data

    #Trying to register without a username should fail and return a message
    response = client.post('/register', data={'username': '', 'password': 'password_123'})

    assert b'Username is required' in response.data

    #Trying to register without a password should fail and return a message
    response = client.post('/register', data={'username': 'user2', 'password': ''})

    assert b'Password is required' in response.data

    #Ensure that the registered user is in the database
    with app.app_context():
        cur = get_db().cursor()
        cur.execute("SELECT password FROM users WHERE username = 'user1'")
        assert cur.fetchone()[0] == 'User1_123'
        cur.close()
