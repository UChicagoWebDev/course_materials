import pytest
import passwords

# @app.route('/api/admin', methods=['POST'])
# def admin():
#     body = request.get_json()
#     secret_code = body.get('secret_code', None)
#     if secret_code == 'open sesame':
#         return {}, 200
#     return {}, 403


@pytest.fixture
def client():
    server = passwords.create_app()
    with server.test_client() as client:
        yield client


def test_admin_forbidden(client):
    """Returns a 403 to calls without the correct secret password"""
    response = client.post('/api/admin', json={'secret_code': 'no sesame'})
    assert response.status == "403 FORBIDDEN"
    return


def test_admin_with_code(client):
    """Returns a 200 to calls with the correct secret password"""
    response = client.post('/api/admin', json={'secret_code': 'top secret'})
    assert response.status == "200 OK"
    return
