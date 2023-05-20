import os
import tempfile
import pytest
import configparser

from passwords import create_app
from passwords.db import get_db
from passwords.db import init_db


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
        'PEPPER': 'JALAPEÑO'
    })

    with app.app_context():
        init_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture
def new_user():
    return "Cool New Username", "Cool New Password"


def test_static_html(client):
    """Serves the static html page and the root path"""

    rv = client.get('/')
    # TODO: Check status and content
    assert rv.status == "200 OK"
    assert "<title>Single-Page Login and Post</title>" in rv.data.decode(
        'utf-8')


def test_signup_and_login(client, new_user):
    """Tests that I can log in with new credentials"""

    new_username, new_password = new_user

    create_response = client.post(
        '/api/signup', json={'username': new_username, 'password': new_password})
    assert create_response.status == "200 OK"

    # response = try to log in with new_username and new_password
    response = client.post(
        '/api/login', json={'username': new_username, 'password': new_password})

    # TODO: check for success
    assert response.status == "200 OK"


def test_wrong_password(client, new_user):
    """Tests that I can't log in with invalid credentials"""
    # TODO: Try to log in with deliberately wrong password

    new_username, new_password = new_user
    create_response = client.post(
        '/api/signup', json={'username': new_username, 'password': new_password})
    assert create_response.status == "200 OK"

    bad_password = new_password + "Deliberately Broken"
    response = client.post(
        '/api/login', json={'username': new_username, 'password': bad_password})
    assert response.status != "200 OK"


def test_duplicate_signup(client, new_user):
    """Tests that I can't create a new user with an existing username"""
    # TODO: Try to register twice with the same username

    new_username, new_password = new_user
    create_response = client.post(
        '/api/signup', json={'username': new_username, 'password': new_password})
    assert create_response.status == "200 OK"

    bad_password = new_password + "Deliberately Broken"
    response = client.post(
        '/api/signup', json={'username': new_username, 'password': bad_password})
    assert response.status == "302 FOUND"
