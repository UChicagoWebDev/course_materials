from flask import Flask, render_template, send_file
import time
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/<string:animal>')
@app.route('/')
def index(animal="None"):
    time.sleep(3)
    print(animal)
    return render_template('index.html', animal=animal)

@app.route('/spa/<string:animal>')
@app.route('/spa')
def spa(animal="None"):
    time.sleep(3)
    return send_file('static/spa.html')