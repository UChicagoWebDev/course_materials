# Row Row Row Your API
from flask import Flask, request, jsonify
from markupsafe import escape

app = Flask(__name__)

song =  {"lines": [
    "Row row row your boat",
    "Gently down the stream",
    "Merrily merrily merrily merrily",
    "Life is but a dream"]}

@app.route('/')
def hello():
    return song

@app.route('/line/<int:line_number>', methods=['GET', 'POST'])
def get_line(line_number):
    print(song)
    if(request.method == "GET"):
        return song["lines"][line_number]
    elif(request.method == "POST"):
        request.get_data()
        print("we got a POST")
        print(request.data)
        new_line = request.data.decode("utf-8")
        song["lines"][line_number] = new_line
        return song["lines"][line_number]
    print("wtf?")
    # TODO: Add a POST method that add or updates a line to the song

