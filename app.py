from flask import Flask

app = Flask(__name__)

@app.route('/home')
def HomePage():
    return "Welcome to home page"

app.run("0.0.0.0",4000,debug=True)