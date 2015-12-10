from flask import render_template, redirect,request,url_for,g,flash
from app import app
from models import *
from datetime import datetime
import json
import scipy as sp
from scipy import stats
import math
from app import flask_login,login_manager
import bcrypt

@login_manager.user_loader
def user_loader(email):
    users = Users.query.all()
    for user_obj in users:
        if email == user_obj.email:
            user = User()
            user.id = email
            return user
    return 

@login_manager.request_loader
def request_loader(request):
    users = Users.query.all()
    email = request.form.get("email")
    for user_obj in users:
        if email == user_obj.email:
            user = User()
            user.id = email
            user.is_authenticated = request.form.get("password") == user_obj.password
            return user
    return

def process_dates(dates):
    #returns list with deltas of the form: current_date - date_created
    current_date = datetime.now()
    time_elapsed = []
    for date in dates:
        time_elapsed.append((current_date - date).days)
    return time_elapsed

def check_password(email,password):
    user_pw = str(Users.query.filter_by(email=email).first().password)
    if bcrypt.hashpw(password,user_pw) == user_pw:
        return True
    else:
        return False
    
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    #explicitly force string type because of demands from bcrypt
    email = str(request.form.get("email"))
    password = str(request.form.get("password"))
    if check_password(email,password):
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for("splash_page"))
    return render_template("login.html",error="username or password was incorrect, please try again")
    
@app.route("/splash_page",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def splash_page():
    return render_template("splash_page.html")

@app.route("/sample_report",methods=["GET","POST"])
def sample_report():
    dates = [elem.date_created for elem in Data.query.all()]
    time_elapsed = process_dates(dates)
    s = sp.array(time_elapsed)
    n,min_max,mean,var,skew,kurt = stats.describe(s)
    sorted_time_elapsed = time_elapsed[:]
    sorted_time_elapsed.sort()
    sorted_time_elapsed = ["Sorted Time Elapsed - Note: sorted order does not correspond to the table below"] + sorted_time_elapsed 
    data = zip(Data.query.all(),time_elapsed)
    time_elapsed = ["time elapsed"] + time_elapsed
    return render_template(
        "sample_report.html",
        show_sorted=True,
        average=round(mean,3),
        standard_deviation=round(math.sqrt(var),3),
        skew=round(skew,3),
        kurtosis=round(kurt,3),
        time_elapsed=json.dumps(time_elapsed),
        sorted_time_elapsed=json.dumps(sorted_time_elapsed),
        data=data
    )

@app.route("/query_bar",methods=["GET","POST"])
def query_bar():
    if request.method=="POST":
        pass
    return "nothing"
