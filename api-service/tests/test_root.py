# Integration test root URL of API service

def test_root(test_app):
    response = test_app.get('api/')
    assert response.status_code == 200
    assert response.json() == {
        "Success": "Hello World!"
    }
    
def test_url(test_app):
    pass
 
def test_eval(test_app):
    pass
