from flask import Flask

app = Flask(__name__)

app.run(debug=True, host='0.0.0', port=8000)