from flask import Flask, render_template, request, jsonify
from functools import wraps

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

posts = [
    {
        "id": 0,
        "title": "Hello World!",
        "body": "This is my first post and I'm so proud of it."
    }
]

@app.route('/')
def index():
    return app.send_static_file('index.html')

# -------------------------------- API ROUTES ----------------------------------

@app.route('/api/login', methods=['POST'])
def login ():
    print(request.data)
    body = request.get_json()
    print(body)

    username = body['username']
    password = body['password']

    if(username == "trevor" and password == "password"):
        return {"session_token": "12345",}

    return {}, 403

@app.route('/api/post', methods=['POST'])
def post():
    print(request.data)
    body = request.get_json()
    session_token = body['session_token']

    if(session_token != "12345"):
        return {}, 403

    if 'title' in body and 'body' in body:
        new_post = {
            "id": len(posts),
            "title": body['title'],
            "body": body['body']
        }
        posts.insert(0,new_post)

    return jsonify(posts)
