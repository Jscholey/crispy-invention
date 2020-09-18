from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return("<h1>Hi there</h1>")

@app.route("/page", methods=["GET"])
def page():
    return("<h2>this is a page</h2>")


if __name__=="__main__":
    app.run("127.0.0.1", 5000, True)