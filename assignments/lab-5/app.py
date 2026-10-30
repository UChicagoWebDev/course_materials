# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return "Hello, Awesome World!"

@app.route("/row")
@app.route("/row/<int:row_id>")
def row(row_id=None):
    verses = [
        "Row row row your boat",
        "Gently down the stream",
        "Merrily merrily merrily",
        "Life is but a dream"
    ]
    if(row_id is not None):
        return verses[row_id]
    return {"verses": verses}