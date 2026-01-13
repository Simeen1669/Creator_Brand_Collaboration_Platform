from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def brand():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM creator_profile")
    creators = cur.fetchall()
    conn.close()
    return str(creators)

@app.route("/request/<int:id>")
def request_send(id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO requests VALUES(NULL,?,?,?)",
                (id,'Campaign','Pending'))
    conn.commit()
    conn.close()
    return "Model 4 Test Passed: Request Sent"

app.run(debug=True)
