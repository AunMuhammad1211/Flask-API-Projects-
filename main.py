from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
conn = mysql.connector.connect(
    host="",
    user="",
    password="",
    database="",
)
cursor = conn.cursor()

@app.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        rollno = request.form['rollno']
        program = request.form["program"]
        feedback = request.form["feedback"]

        query = "INSERT INTO survey_response (name, email, rollno, program, feedback) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, email, rollno, program, feedback))
        conn.commit()
        
        return redirect(url_for("result", name=name, email=email, rollno=rollno, program=program, feedback=feedback))

    return render_template("index.html")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)