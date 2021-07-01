# Importing general dependencies/libraries
import pandas as pd
import numpy as np
import datetime as dt

# Import sqlalchemy and related content
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

# Import Flask
import flask
from flask import Flask, jsonify

# Import icecream for debugging
from icecream import ic
ic.configureOutput(includeContext=True)

# Setting up database access
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station


# --------------- Flask setup ----------------------------
app=Flask(__name__)

# Declare all routs
# default/landing/home
@app.route("/")
def home():
    return(f'<h1 style="font-family: Arial;">Greetings!</h1>\
        <p style="font-family: Arial;">This is an API that allows you to find out weather in Hawaii.</p>\
        <p style="font-family: Arial;">This is a listing of available API queries:</p>\
        <un>\
            <li>/</li>\
            <li>/api/v1.0/precipitation</li>\
            <li>/api/v1.0/stations</li>\
            <li>/api/v1.0/tobs</li>\
            <li>/api/v1.0/&lt;start&gt;</li>\
            <li>/api/v1.0/&lt;start&gt;/&lt;end&gt;</li>\
        </un>\
        <p style="font-family: Arial;">Please note that dates must be priovided in YYY-MM-DD format.<br> Available date range is between 2010-01-01 & 2017-08-23</p>')

# precipitation
@app.route("/api/v1.0/precipitation")
def prcp():
    return('Placeholder')

@app.route("/api/v1.0/stations")
def stn():
    return('Placeholder')

@app.route("/api/v1.0/tobs")
def tobs():
    return('Placeholder')

@app.route("/api/v1.0/<start>")
def strt():
    return('Placeholder')

@app.route("/api/v1.0/<start>/<end>")
def strt_end():
    return('Placeholder')

# Run app
if __name__ == "__main__":
    app.run(debug=True)