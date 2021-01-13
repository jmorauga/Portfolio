from flask import Flask, redirect, url_for, render_template, request, send_file, jsonify
from datetime import datetime

app = Flask(__name__)

app.config['JSON_ASCII'] = False

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
