import requests
import pytest # have to install via command "pip3 install -U pytest"

def test_health_check():
    r = requests.get('http://localhost:8085')
    assert(r.status_code == 404)

# 1. Add two more tests here of your choice. I will explain the API.
#    Make sure to verify the necessary info, e.g., status code, response data.
# 2. Add "pytest" as integration testing script as part of Github Actions CI workflow (you've done this before!)
# Test if id goes up
def test_id_check():
    r = requests.get('http://localhost:8085/hello-world')
    request_json = r.json()
    old_id = request_json['id']

    r = requests.get('http://localhost:8085/hello-world')
    request_json = r.json()
    new_id = request_json['id']

    assert(new_id == old_id + 1)

# Test if name is returned
def test_name_check():
    r = requests.get('http://localhost:8085/hello-world?name=Henry')
    request_json = r.json()
    assert(request_json['content'] == 'Hello, Henry!')
