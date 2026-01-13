from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users VALUES(NULL,?,?,?)",
                    (request.form['email'], request.form['password'], request.form['role']))
        conn.commit()
        conn.close()
        return "Model 2 Test Passed: Registration Successful"
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=? AND password=?",
                    (request.form['email'], request.form['password']))
        user = cur.fetchone()
        conn.close()
        return "Login Success" if user else "Login Failed"
    return render_template("login.html")

app.run(debug=True)
