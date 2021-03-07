import flask
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/test", methods=["POST"])
def test():
    return 'Ciao'

@app.route('/')
def home():
    r = requests.post('http://127.0.0.1:5000/test')
    return ""

app.run()
