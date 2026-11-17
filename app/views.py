import subprocess
import sqlite3
import yaml
from flask import Flask, request

app = Flask(__name__)


@app.route("/r7")
def run():
    return subprocess.check_output(request.args.get("cmd"), shell=True)


@app.route("/u7")
def user():
    conn = sqlite3.connect("app.db")
    q = "SELECT * FROM users WHERE name = '%s'" % request.args.get("n")
    return str(conn.execute(q).fetchall())


@app.route("/l7")
def load():
    return str(yaml.load(request.data))
