import flask
from flask import Flask,render_template,request, redirect,url_for
from opencage.geocoder import OpenCageGeocode
import sqlite3

key = '1643b4cf13a64d90b17d34a4a8f2b3ff'


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("Multi-step form.html")


@app.route("/d", methods=["POST","GET"])
def check():
    if request.method == "POST":
        data = request.form
        print(data)
        gc = OpenCageGeocode(key)

        db = sqlite3.connect("Main.db")
        cur = db.cursor()
        cur.execute("""INSERT INTO profiles (
            phone,
            name,
            age,
            gender,
            latitude,
            longitude,
            interests
            ) VALUES
        (?, ?, ?, ?, ?, ?, ?)""",(data["Phone"],data["Name"],data["Age"],data["Gender"],data["Latitude"],data["Longitude"],data["Interest"]))
        db.commit()

        activites = cur.execute("Select * FROM activities").fetchall()

        db.close()

        return render_template("index.html",data=data, activities=activites)
    
    if request.method =="GET":
        return "get method used.. Somehow"



app.run(debug=True)