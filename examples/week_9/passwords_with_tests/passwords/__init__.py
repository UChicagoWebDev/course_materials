import os
from flask import Flask, request, jsonify
import bcrypt
import configparser
import sqlite3
from . import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.update(SEND_FILE_MAX_AGE_DEFAULT=0)
    if test_config is None:
        config = configparser.ConfigParser()
        config.read_file(
            open(os.path.join(os.path.dirname(__file__), '../secrets.cfg')))
        app.config.update(
            DATABASE=os.path.join(app.instance_path, 'passwords.sqlite'),
            PEPPER=config['secrets']['PEPPER']
        )
    else:
        app.config.update(test_config)
    db.init_app(app)
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    @app.errorhandler(Exception)
    def handle_invalid_usage(error):
        response = jsonify(str(error))
        response.status_code = 500
        return response
    # -------------------------------- API ROUTES ----------------------------------
    @app.route('/api/admin', methods=['POST'])
    def admin():
        body = request.get_json()
        secret_code = body.get('secret_code', None)
        if secret_code == 'top secret':
            return {}, 200
        return {}, 403
    @app.route('/api/signup', methods=['POST'])
    def signup():
        body = request.get_json()
        username = body['username']
        password = body['password'] + \
            app.config['PEPPER']  + "Deliberately Broken"
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        connection = db.get_db()
        cursor = connection.cursor()
        query = "INSERT into users (username, password) VALUES (?, ?)"
        try:
            cursor.execute(query, (username, hashed))
            connection.commit()
            return {}
        except sqlite3.IntegrityError as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print(message)
            if str(e) == "UNIQUE constraint failed: users.username":
                return {"username": username}, 302
            raise e
        finally:
            cursor.close()
            connection.close()
    @app.route('/api/login', methods=['POST'])
    def login():
        body = request.get_json()
        username = body['username']
        password = body['password'] + app.config['PEPPER']
        connection = db.get_db()
        cursor = connection.cursor()
        query = "SELECT password FROM users WHERE username=?"
        try:
            cursor.execute(query, (username,))
            row = cursor.fetchone()
            if row is not None:
                hashed = row['password']
                success = bcrypt.checkpw(password.encode('utf-8'), hashed)
                if success:
                    return {}
            return {}, 404
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            raise e
        finally:
            cursor.close()
            connection.close()
    return app
