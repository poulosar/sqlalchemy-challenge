# 1. importing dependencies

from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import datetime as dt


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

#Creating engine and database connection
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station


# Creating session link
session = Session(engine)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return(f"WELCOME to my API<br/>"
        f"<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"<br/>"   
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"<br/>"
        f"List of Stations: /api/v1.0/stations<br/>"
        f"<br/>"
        f"Temperature for one year: /api/v1.0/tobs<br/>"
        f"<br/>"
        f"Temperature stat from the start date yyyy-mm-dd: /api/v1.0/yyyy-mm-dd<br/>"
        f"<br/>"
        f"Temperature stat from start to end dates yyyy-mm-dd: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd")



# 4. Define what to do when a user hits the /precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("User is accessing precipitation data")
    results = session.query(Measurement.date, Measurement.prcp)
    
    all_precipitation = []
    for date,prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        all_precipitation.append(precipitation_dict)
    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    print("User is accessing stations data")
    results = session.query(Station.station, Station.name, Station.latitude,Station.longitude, Station.elevation)
    session.close()
    all_stations = []
    for station,name,latitude,longitude,elevation in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["longitude"] = longitude
        station_dict["latitude"] = latitude
        station_dict["elevation"] = elevation
        all_stations.append(station_dict)
    return jsonify(all_stations)

    
@app.route("/api/v1.0/tobs")
def tobs():
    print("User is accessing precipitation data")
    return "Welcome to my 'Blog' page!"

@app.route("/api/v1.0/<start>")
def start():
    print("User is accessing precipitation data")
    return "Welcome to my 'Blog' page!"

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    print("User is accessing precipitation data")
    return "Welcome to my 'Blog' page!"



if __name__ == "__main__":
    app.run(debug=True)
