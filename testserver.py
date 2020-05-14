from flask import Flask, request, send_file
import time
import datetime
import sqlite3

app = Flask(__name__)


@app.route("/file", methods=['POST'])
def reqfile():
    data = request.json
    with open('qwe.icon', 'wb') as f:
        f.write(data)
    return 'ok'


@app.route('/get_image')
def get_image():
    return send_file('widget_icon.png', mimetype='image/png')

app.run()