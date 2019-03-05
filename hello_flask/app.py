#https://code.visualstudio.com/docs/python/tutorial-flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route('/<name>')
def index(name="Treehouse"):
    return "Hello, from {}!".format(name)

app.run(debug=True)




