from flask import Flask

app = Flask(__name__)

@app.route('/flask-example')
def hello():
    return 'hello world'
