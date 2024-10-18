# Row Row Row Your API
from flask import Flask, request, jsonify, redirect
from markupsafe import escape
app = Flask(__name__)
song =  {"lines": [
    "Row row row your boat",
    "Gently down the stream",
    "Merrily merrily merrily merrily",
    "Life is but a dream"]}
@app.route('/', methods=['GET'])
def hello():
    if request.method == "GET":
        return song
    if request.method == "POST":
        return {}, 403

@app.route('/lines/<int:n>')
def firstLine(n):
    if n < 1 or n > 4:
        return redirect("/")
    return song['lines'][n-1]
