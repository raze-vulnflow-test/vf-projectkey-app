import subprocess
import sqlite3
import yaml
from flask import Flask, request

app = Flask(__name__)


@app.route("/run")
def run():
    return subprocess.check_output(request.args.get("cmd"), shell=True)


@app.route("/user")
def user():
    conn = sqlite3.connect("app.db")
    q = "SELECT * FROM users WHERE name = '%s'" % request.args.get("n")
    return str(conn.execute(q).fetchall())


@app.route("/load")
def load():
    return str(yaml.load(request.data))
