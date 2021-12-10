def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "Very Awesome API"
    assert res.status_code == 200
