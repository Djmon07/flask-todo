import pytest

def test_todo_list(client):
    # View the home page and check to see the header and a to-do item
    response = client.get('/')
    assert b'<h1>A simple to-do application</h1>' in response.data
    assert b'clean room' in response.data
    assert b'<button type="submit">Apply' in response.data
    assert b'<a href="/complete/' in response.data

    # Mock data should show three to-do items, one of which is complete
    assert response.data.count(b'<li class="">') == 2
    assert response.data.count(b'<li class="completed">') == 1


def test_filter(client):

    response = client.post('/', data={'filter': 'completed'})
    assert b'do homework' in response.data
    assert b'clean room' not in response.data

    response = client.post('/', data={'filter': 'uncompleted'})
    assert b'do homework' not in response.data
    assert b'clean room' in response.data

<<<<<<< HEAD
def test_remove(client):
    response = client.post('/remove', data={'remove': 'do homework'})
    assert response.data.count(b'<li class="completed">') == 0
=======
def test_completion(client):

    response = client.post('/', data={'filter': 'uncompleted'})
    assert b'clean room' in response.data
    response = client.get('/complete/1')
    response = client.post('/', data={'filter': 'uncompleted'})
    assert b'clean room' not in response.data
>>>>>>> ede6ebf0a4d01762a0c1597b65f30059b01ec3e7
