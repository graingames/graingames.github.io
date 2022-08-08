import email
from flask import Flask, redirect ,url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
file_path = os.path.abspath(os.getcwd())+"\database.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(100))
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

@app.route("/")
def redirect():
    return render_template("redirect.html")
@app.route("/home.html", methods = ["POST","GET"])
def home():
    if request.method == "POST":
        user = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone_no"]
        found_user = users.query.filter_by(email = email).first()
        if found_user:
            print("User existed")
        else:
            usr = users(user, email, phone)
            db.session.add(usr)
            db.session.commit()
        return render_template("thank.html")
    else:
        return render_template("home.html")
@app.route("/ActionPlan.html")
def actionplan():
    return render_template("ActionPlan.html")
@app.route("/docs.html")
def docs():
    return render_template("docs.html")
@app.route("/Questions.html")
def questions():
    return render_template("Questions.html")
@app.route("/Tale.html")
def tale():
    return render_template("Tale.html")
@app.route("/features.html")
def features():
    return render_template("features.html")
@app.route("/Help.html")
def help():
    return render_template("Help.html")
@app.route("/QNtNwSUwfPsrVIdmbgRNwLvaOAAcEAzdUQWfmyKxQLUyBIEcnb", methods = ["POST","GET"])
def database():
    if request.method == "POST":
        email = request.form["email"]
        found_user = users.query.filter_by(email=email).first()
        if found_user:
           db.session.delete(found_user)  
           db.session.commit()
    return render_template("database_handle.html")

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)