import os
import requests
## Define a test that will always pass successfully
def test_InfoApi():
    endpoint = "http://0.0.0.0:5000/info"
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert 'Receiver' in json
    assert json['Receiver'] == "Cisco is the best!"


def test_PingApi():
    endpoint = "http://0.0.0.0:5000/ping"
    data = {
        "url": "https://www.google.com"
    }
    response = requests.post(endpoint, json = data)
    assert response.status_code == 200
