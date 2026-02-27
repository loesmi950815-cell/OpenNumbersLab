
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/finance/compound-interest", methods=["GET", "POST"])
def compound_interest():
    result = None
    if request.method == "POST":
        principal = float(request.form["principal"])
        rate = float(request.form["rate"]) / 100
        years = float(request.form["years"])
        result = principal * ((1 + rate) ** years)
    return render_template("compound.html", result=result)

@app.route("/student/percentage", methods=["GET", "POST"])
def percentage():
    result = None
    if request.method == "POST":
        part = float(request.form["part"])
        whole = float(request.form["whole"])
        result = (part / whole) * 100
    return render_template("percentage.html", result=result)

@app.route("/productivity/work-hours", methods=["GET", "POST"])
def work_hours():
    result = None
    if request.method == "POST":
        hours_per_day = float(request.form["hours"])
        days = float(request.form["days"])
        result = hours_per_day * days
    return render_template("workhours.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
