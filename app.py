from flask import Flask, render_template, request, abort, redirect
import os
import psycopg2
'''
DATABASE_URL = os.environ["DATABASE_URL"]

conn = psycopg2.connect(DATABASE_URL, sslmode="require")
'''
app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return("<h1>Hi there</h1>")

@app.route("/page", methods=["GET"])
def page():
    return render_template("index.html")


"""
@app.route("/event/<eventName>")
def event(eventName):
    if eventName in ["one", "two", "three", "four", "five", "six", "seven", "pyraminx", "megaminx", "square1", "bld"]:
        return render_template("AllEvents.html", event=eventName)
    else:
        abort(404)
"""


@app.route("/event", methods=["GET", "POST"])
def event():
    if request.method == "GET":
        data = request.args
        if "event" in data:
            event = data["event"]
            #
            # TODO check if event exists in database
            if event not in ["two", "three", "four", "five", "six", "seven", "megaminx", "pyraminx", "square1"]:
                return redirect("/event")
            # if not, redirect to GET event without request args
            #
            
            panel = "leaderboard"
            leaderboard = True
            if "panel" in data and data["panel"]=="timer":
                panel = "timer"
                leaderboard = False

            return render_template("eventTemplate.html", event=event, panel=panel, leaderboard=leaderboard)
            #
            # Show relevant filled template based on event and panel
            #
        else:
            return render_template("AllEvents.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__=="__main__":
    app.run("127.0.0.1", 5000, True)