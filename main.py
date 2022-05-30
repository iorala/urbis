from flask import Flask, redirect
from flask import render_template
from flask import request
from collections import defaultdict

app = Flask("urbis")

@app.route('/')
def home():
    return render_template("index.html")

# run app (debug mode)
if __name__ == "__main__":
    app.run(debug=True, port=5000)