from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def creator():
    if request.method == "POST":
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO creator_profile VALUES(NULL,?,?,?)",
                    (request.form['niche'], request.form['platform'], request.form['followers']))
        conn.commit()
        conn.close()
        return "Model 3 Test Passed: Creator Profile Saved"
    return "<form method='post'><input name='niche'><input name='platform'><input name='followers'><button>Save</button></form>"

app.run(debug=True)
