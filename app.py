from flask import Flask, render_template, request
import os
import psycopg2

DATABASE_URL = os.environ["DATABASE_URL"]

conn = psycopg2.connect(DATABASE_URL, sslmode="require")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    cur = conn.cursor()
    cur.execute("""CREATE TABLE EVENTS
        (ID INT PRIMARY KEY NOT NULL,
        EVENT TEXT NOT NULL);
        """)
    return("<h1>Hi there</h1>")

@app.route("/page", methods=["GET"])
def page():
    return render_template("index.html")


if __name__=="__main__":
    app.run("127.0.0.1", 5000, True)