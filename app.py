from flask import Flask, render_template, request, abort, redirect
import os
import psycopg2


DATABASE_URL = os.environ["DATABASE_URL"]
conn = psycopg2.connect(DATABASE_URL, sslmode="require")


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

def get_display_name(event):
"""
    names = {"three": "3x3",
             "two": "2x2",
             "four": "4x4",
             "five": "5x5",
             "six": "6x6",
             "seven": "7x7",
             "megaminx": "Megaminx",
             "pyraminx": "Pyraminx",
             "square1": "Square-1"}
    try:
        out = names[event]
    except:
        out = event
        """
    return "fancy name"


@app.route("/event", methods=["GET", "POST"])
def event():
    if request.method == "GET":

        cur = conn.cursor()
            try:
                cur.execute("""
                    Select * from events;
                    """)
                rows = cur.fetchall()
                events = []
                for row in rows:
                    out = {"event": row[1],
                           "display": get_display_name(row[1])}
                    events.append(out)
            except:
                abort(404)
        test = events
        events = ["three", "four"]

        data = request.args
        if "event" in data:
            event = data["event"]

            # Check if event exists in database
            if event not in events:
                return redirect("/event")
            # if not, redirect to GET event without request args
            
            panel = "leaderboard"
            leaderboard = True
            if "panel" in data and data["panel"]=="timer":
                panel = "timer"
                leaderboard = False

            return render_template("eventTemplate.html", allEvents=events, event=test, panel=panel, leaderboard=leaderboard)
            #
            # Show relevant filled template based on event and panel
            #
        else:
            return render_template("AllEvents.html", allEvents=events)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__=="__main__":
    app.run("127.0.0.1", 5000, True)