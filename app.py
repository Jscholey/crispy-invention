from flask import Flask, render_template, request, abort, redirect
import os
import psycopg2
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange

DATABASE_URL = os.environ["DATABASE_URL"]
SECRET_KEY = os.environ["SECRET_KEY"]

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY

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
    return out


class TimeSubmitForm(FlaskForm):
    name = StringField("Name: ")#, validators=[DataRequired()])
    time = DecimalField("Time: ")#, validators=[DataRequired(), NumberRange(min=0)], places=3)
    submit = SubmitField("Submit")


@app.route("/event", methods=["GET", "POST"])
def event():
    if request.method == "GET":

        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        try:
            cur = conn.cursor()
            cur.execute("""
                Select * from events;
                """)
            rows = cur.fetchall()
            events = []
            eventsList = []
            for row in rows:
                out = {"event": row[1],
                       "display": get_display_name(row[1])}
                events.append(out)
                eventsList.append(row[1])
        except:
            abort(404)
        conn.close()


        data = request.args
        if "event" in data:
            event = data["event"]

            # Check if event exists in database
            if event not in eventsList:
                return redirect("/event")
            # if not, redirect to GET event without request args
            
            panel = "leaderboard"
            leaderboard = True
            if "panel" in data and data["panel"]=="timer":
                panel = "timer"
                leaderboard = False


            if leaderboard:
                conn = psycopg2.connect(DATABASE_URL, sslmode="require")
                try:
                    cur = conn.cursor()
                    cur.execute("""
                        Select * from events where "eventName"=%s
                        """, [event])
                    e = cur.fetchone()
                    cur.execute("""
                        Select * from times where "EventId"=%s
                        """,
                        [e[0]])
                    times = cur.fetchall()
                except:
                    abort(404)
                conn.close()

                times.sort(key=lambda x: x[3])

                return render_template("leaderboard.html",
                    title=get_display_name(event),
                    allEvents=events,
                    event=event,
                    panel=panel,
                    leaderboard=leaderboard,
                    times=times)

            else:

                return render_template("timer.html",
                    title=get_display_name(event),
                    allEvents=events,
                    event=event,
                    panel=panel,
                    leaderboard=leaderboard)

        else:

            return render_template("AllEvents.html", allEvents=events)


    elif request.method == "POST":

            try:
                event = request.form['event']
            except:
                return redirect("/event")

            # Form handling logic
            valid = True
            try:
                name = request.form['name']
                time = request.form['time']
            except:
                valid = False



            if valid:
                print("congrats, your time is stored")

            url = "/event?event=%s&panel=timer" % event
            return redirect(url)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__=="__main__":
    app.run("127.0.0.1", 5000, True)