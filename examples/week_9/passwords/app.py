from flask import Flask, render_template, request, jsonify, g
from functools import wraps
# import mysql.connector  # pip3 install mysql-connector
import sqlite3
import bcrypt
import configparser
import io
from argon2 import PasswordHasher


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

config = configparser.ConfigParser()
config.read('secrets.cfg')
DB_NAME = 'passwords'
DB_USERNAME = config['secrets']['DB_USERNAME']
DB_PASSWORD = config['secrets']['DB_PASSWORD']
PEPPER = config['secrets']['PEPPER']


def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = sqlite3.connect('passwords.sqlite3')
        db.row_factory = sqlite3.Row
        setattr(g, '_database', db)
    return db


def query_db(query, args=(), one=False):
    db = get_db()
    cursor = db.execute(query, args)
    print("query_db")
    print(cursor)
    rows = cursor.fetchall()
    print(rows)
    db.commit()
    cursor.close()
    if rows:
        if one:
            return rows[0]
        return rows
    return None


@app.route('/')
def index():
    return app.send_static_file('index.html')

# -------------------------------- API ROUTES ----------------------------------


@app.route('/api/signup', methods=['POST'])
def signup():
    print(request.data)
    body = request.get_json()
    print(body)

    username = body['username']
    password = body['password']
    ph = PasswordHasher()
    hashed = ph.hash(password + PEPPER)

    # connection = mysql.connector.connect(
    #     user=DB_USERNAME, database=DB_NAME, password=DB_PASSWORD)
    # connection = sqlite3.connect('passwords.sqlite')
    # cursor = connection.cursor()

    # TODO: Instead, store a password hashed with bcrypt with a salt and a pepper
    # hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    query = "INSERT into users (username, password) VALUES (?, ?)"

    try:
        # cursor.execute(query, (username, password))
        # connection.commit()
        query_db(query, (username, hashed))
        return {}, 200
    except Exception as e:
        print(e)
        return {"username": username}, 302
    finally:
        print("Finally!")
    #     # cursor.close()
    #     # connection.close()
    #     return {}, 404


@app.route('/api/login', methods=['POST'])
def login():
    print(request.data)
    body = request.get_json()
    print(body)

    username = body['username']
    password = body['password']

    # connection = mysql.connector.connect(
    #     user=DB_USERNAME, database=DB_NAME, password=DB_PASSWORD)
    # cursor = connection.cursor()

    query = "SELECT password FROM users WHERE username=?"

    try:
        result = query_db(query, (username,), True)
        # TODO: Instead, check that password matches its bcrypt hash

        print(result)
        print(result[0])

        ph = PasswordHasher()
        if result and ph.verify(result[0], password + PEPPER):
            return jsonify({})
        return {}, 404
    except Exception as e:
        print(e)
        return {}, 404
    finally:
        #     # cursor.close()
        #     # connection.close()
        print("Finally!")
    #     return {}, 404
