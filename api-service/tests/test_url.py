# Test URL endpoint of API service

def test_invalid_url(test_app):

    payload = {
        "url" : "htp://broken.url"
    }

    response = test_app.get('api/url/?url=htp://broken.url')
    assert response.status_code == 200
    assert response.json() == {
        "Error": "URL invalid"
    }
