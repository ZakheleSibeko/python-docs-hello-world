from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Zakhele, Lerato, Siyabonga and Khanya Sibeko!"
