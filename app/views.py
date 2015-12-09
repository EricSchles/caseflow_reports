from flask import render_template, redirect,request,url_for,g,flash
from app import app
from models import *
from datetime import datetime
import json
import scipy as sp
from scipy import stats
import math

def process_dates(dates):
    #returns list with deltas of the form: current_date - date_created
    current_date = datetime.now()
    time_elapsed = []
    for date in dates:
        time_elapsed.append((current_date - date).days)
    return time_elapsed

@app.route("/sign_in",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def sign_in():
    return render_template("sign_in.html")

@app.route("/sample_report",methods=["GET","POST"])
def sample_report():
    dates = [elem.date_created for elem in Data.query.all()]
    time_elapsed = process_dates(dates)
    s = sp.array(time_elapsed)
    n,min_max,mean,var,skew,kurt = stats.describe(s)
    time_elapsed = ["time elapsed"] + time_elapsed
    data = zip(Data.query.all(),time_elapsed[1:])
    return render_template(
        "sample_report.html",
        average=round(mean,3),
        standard_deviation=round(math.sqrt(var),3),
        skew=round(skew,3),
        kurtosis=round(kurt,3),
        time_elapsed=json.dumps(time_elapsed),
        data=data
    )

@app.route("/query_bar",methods=["GET","POST"])
def query_bar():
    if request.method=="POST":
        pass
    return "nothing"
