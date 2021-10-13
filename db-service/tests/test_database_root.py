def test_database_url_root(test_app):
    response = test_app.get('/')

    assert response.status_code == 200
    assert response.json() == {
    "message": "Hello World"
    }