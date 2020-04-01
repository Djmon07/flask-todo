import pytest

from flasktodo.db import get_db

def test_register(client, app):

    assert client.get('/register').status_code == 200

    response = client.post('/register', data={'username': 'user1', 'password': 'User1_123'})

    assert response.headers['Location'] == 'http://localhost/'

    with app.app_context():
        cur = get_db().cursor()
        cur.execute("SELECT password FROM users WHERE username = 'user1'")
        assert cur.fetchone()[0] == 'User1_123'
        cur.close()
