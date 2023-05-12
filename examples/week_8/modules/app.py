from flask import Flask, render_template, request, jsonify
from functools import wraps

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return app.send_static_file('index.html')
