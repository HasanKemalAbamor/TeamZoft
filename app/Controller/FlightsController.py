from flask import request, flash, redirect, url_for, make_response, render_template, session
from Model.AddFlight import AddFlightModel
from Model.CheckFlight import FlightModel

def handle_addFlight():
    company= request.form['company']
    departure= request.form['departure']
    destination= request.form['destination']
    date= request.form['date']
    time= request.form['time']


    AddFlightModel.add_flight(company, departure, destination,date.split("-")[0],date.split("-")[1],date.split("-")[2],time.split(":")[0],time.split(":")[1])

    flash('Flight added successfully.', 'success')
    email= request.cookies.get('email')
    response = make_response(render_template("adminpanel.html", email=email))
    response.set_cookie('email', email)
    response.set_cookie("is_admin", "true")
    return response

def handle_searchFlight():
    departure = request.form['departure']
    destination = request.form['destination']
    dateL = request.form['datelowerboundary']

    data = FlightModel.check_flight(departure, destination, dateL.split("-")[0],dateL.split("-")[1],dateL.split("-")[2])
    email = request.cookies.get('email')
    response = make_response(render_template("viewFlights.html", data=data))
    response.set_cookie('email', email)
    response.set_cookie("is_admin", "true")
    return response

