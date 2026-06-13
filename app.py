from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route(
"/create_event",
methods=["GET","POST"]
)
def create_event():

    if request.method=="POST":

        title = request.form["title"]
        date = request.form["date"]
        location = request.form["location"]

        # Save into database

        return redirect("/events")

    return render_template(
    "create_event.html"
    )

@app.route("/events")
def events():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    conn.close()
    return render_template("events.html", events=events)

@app.route(
"/register_event/<int:event_id>"
)
def register_event(event_id):

    user_id = 1

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO registrations
    (user_id,event_id)
    VALUES(?,?)
    """,
    (user_id,event_id)
    )

    conn.commit()

    conn.close()

    return redirect("/events")

@app.route("/logout")
def logout():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
