from flask import Flask, render_template, request
from datetime import date
import csv
weekdays = {
    0:"monday",
    1:"tuesday",
    2:"wednesday",
    3:"thursday",
    4:"friday",
    5:"saturday",
    6:"sunday",
}

fields=["Email", "Interest", "Weekday"]
filename = "info.csv"
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def ping():
    if request.method=="POST":
        email = request.form.get("email")
        interest = request.form.get("interests")
        day = weekdays[date.today().weekday()]
        with open(filename, "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([email, interest, day])


    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
