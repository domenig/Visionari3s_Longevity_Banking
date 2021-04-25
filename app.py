# importing the library
import os
from flask import Flask
from flask import render_template

# print(os.getcwd())            to get an understand of the cwd to guide the flask integration

# creating an instance fro the Flask class passing in name of application
app = Flask(__name__)

"""@app.route('/index')            # home route
def index():
    return render_template("index.html")"""              # 404 error

"""@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, r=2)"""     # 404 error

if __name__ == "__main__":
    app.run()

