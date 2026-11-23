"""OPS-102 acceptance tests: filter incidents by status.

Fixture data (tests/conftest.py):
    1042 critical / open
    1043 high     / open
    1044 low      / resolved
"""


def ids(response):
    return [i["id"] for i in response.json()]


def test_filter_status_open(client):
    response = client.get("/incidents?status=open")
    assert response.status_code == 200
    assert ids(response) == [1042, 1043]


def test_filter_status_resolved(client):
    response = client.get("/incidents?status=resolved")
    assert response.status_code == 200
    assert ids(response) == [1044]


def test_filter_status_without_matches(client):
    response = client.get("/incidents?status=investigating")
    assert response.status_code == 200
    assert response.json() == []


def test_status_and_severity_both_apply(client):
    response = client.get("/incidents?severity=low&status=open")
    assert response.status_code == 200
    assert response.json() == []


def test_invalid_status_returns_422(client):
    assert client.get("/incidents?status=closed").status_code == 422


def test_no_status_preserves_existing_behavior(client):
    response = client.get("/incidents")
    assert response.status_code == 200
    assert ids(response) == [1042, 1043, 1044]
