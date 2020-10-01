from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/time')
def show_time():
    time2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return time2


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
