import requests
import pytest

@pytest.fixture(scope='module')
def req():
    with requests.Session() as s:
        s.headers.update({
            'Accept': 'application/json'
        })

        yield s


def test_luke(req):
    resp = req.get('https://swapi.co/api/people/1/')
    data = resp.json()
    assert data['name'] == 'Luke Skywalker'

