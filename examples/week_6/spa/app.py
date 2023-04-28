from flask import Flask
import time

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/<string:animal>')
@app.route('/')
def index(animal="None"):
    # time.sleep(4)
    print(animal)
    return app.send_static_file('index.html')

# TODO: Handle other potential paths, making sure we always return index.html
