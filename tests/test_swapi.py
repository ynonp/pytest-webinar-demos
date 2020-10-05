import requests
import pytest

def test_name():
    with requests.Session() as s:
        s.headers.update({
            'Accept': 'application/json'
        })
        data = s.get('https://swapi.dev/api/people/1').json()
        assert data['name'] == 'Luke Skywalker'


@pytest.fixture(scope='session')
def req():
    with requests.Session() as s:
        s.headers.update({
            'Accept': 'application/json'
        })

        yield s

