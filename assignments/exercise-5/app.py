import logging
import string
import traceback
import random
import sqlite3
from datetime import datetime
from flask import * # Flask, g, redirect, render_template, request, url_for
from functools import wraps
app = Flask(__name__)

# These should make it so your Flask app always returns the latest version of
# your HTML, CSS, and JS files. We would remove them from a production deploy,
# but don't change them here.
app.debug = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache"
    return response

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('db/watchparty.sqlite3')
        db.row_factory = sqlite3.Row
        setattr(g, '_database', db)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    db = get_db()
    cursor = db.execute(query, args)
    print("query_db")
    print(cursor)
    rows = cursor.fetchall()
    # print(rows)
    db.commit()
    cursor.close()
    return rows

def new_user():
    name = "Unnamed User #" + ''.join(random.choices(string.digits, k=6))
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    cookie = ''.join(random.choices(string.ascii_lowercase + string.digits, k=40))
    api_key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=40))
    new_users = query_db('insert into users (name, password, cookie, api_key) ' + 
        'values (?, ?, ?, ?) returning id, name, password, cookie, api_key',
        (name, password, cookie, api_key),
        one=True)
    if new_users and len(new_users) == 1:
        u = new_users[0]
        return u
    raise Exception("Failed to create new user. Resposne: " + str(new_users))

def get_user_from_cookie(request):
    cookie = request.cookies.get('watch_party_cookie')
    if cookie:
        users = query_db('select * from users where cookie = ?', [cookie], one=True)
        if users and len(users) == 1:
            return users[0]
    return None

def render_with_error_handling(template, **kwargs):
    try:
        return render_template(template, **kwargs)
    except:
        t = traceback.format_exc()
        return render_template('error.html', args={"trace": t}), 500

# ------------------------------ NORMAL PAGE ROUTES ----------------------------------
@app.route('/')
def index():
    print("index") # For debugging
    user = get_user_from_cookie(request)
    if user:
        rooms = query_db('select * from rooms')
        return render_with_error_handling('index.html', user=user, rooms=rooms)
    
    return render_with_error_handling('index.html', user=None, rooms=None)

@app.route('/rooms/new', methods=['GET', 'POST'])
def create_room():
    print("create room") # For debugging
    user = get_user_from_cookie(request)
    if user is None: return {}, 403
    if (request.method == 'POST'):
        name = "Unnamed Room " + ''.join(random.choices(string.digits, k=6))
        rooms = query_db('insert into rooms (name) values (?) returning id', [name], one=True)
        if rooms and len(rooms) == 1:
            room = rooms[0]            
            return redirect(f'{room["id"]}')
        return {}, 500
    else:
        return app.send_static_file('create_room.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print("signup")
    user = get_user_from_cookie(request)
    if user:
        return redirect('/profile')
        # return render_with_error_handling('profile.html', user=user) # redirect('/')
    
    if request.method == 'POST':
        u = new_user()
        print("u")
        print(u)
        for key in u.keys():
            print(f'{key}: {u[key]}')
        resp = redirect('/profile')
        resp.set_cookie('watch_party_cookie', str(u['cookie']))
        return resp
    
    return redirect('/login')

@app.route('/profile')
def profile():
    print("profile")
    user = get_user_from_cookie(request)
    if user:
        return render_with_error_handling('profile.html', user=user)
    
    redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("login")
    user = get_user_from_cookie(request)
    if user:
        return redirect('/')
    
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        users = query_db('select * from users where name = ? and password = ?', [name, password], one=True)
        if users and len(users) == 1:
            u = users[0]
            resp = make_response(redirect("/"))
            resp.set_cookie('watch_party_cookie', u["cookie"])
            return resp
    return render_with_error_handling('login.html', failed=True) 
  
@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('watch_party_cookie', '')
    return resp

@app.route('/rooms/<int:room_id>')
def room(room_id):
    user = get_user_from_cookie(request)
    if user is None: return redirect('/')

    rooms = query_db('select * from rooms where id = ?', [room_id], one=True)
    if rooms and len(rooms) == 1:
        room = rooms[0]
        return render_with_error_handling('room.html',room=room, user=user)
    return {}, 404

# -------------------------------- API ROUTES ----------------------------------
# POST to change the user's name
@app.route('/api/user/name')
def update_username():
    return {}, 403
# POST to change the user's password
# POST to change the name of a room
# GET to get all the messages in a room
# POST to post a new message to a room
