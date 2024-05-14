from flask import request, flash, redirect, url_for, make_response, render_template, session
from Model.AddFlight import AddFlightModel
from Model.CheckFlight import FlightModel

def handle_addFlight():
    company= request.form['company']
    departure= request.form['departure']
    destination= request.form['destination']
    date= request.form['date']
    time= request.form['time']
    email= request.cookies.get('email')

    AddFlightModel.add_flight(company, departure, destination,date.split("-")[0],date.split("-")[1],date.split("-")[2],time.split(":")[0],time.split(":")[1],1,email)

    flash('Flight added successfully.', 'success')
    response = make_response(render_template("adminpanel.html", email=email))
    response.set_cookie('email', email)
    response.set_cookie("is_admin", "true")
    return response

def handle_searchFlight():
    email = request.cookies.get('email')
    data = FlightModel.check_flight(email)
    response = make_response(render_template("viewFlights.html", data=data))
    response.set_cookie('email', email)
    response.set_cookie("is_admin", "true")
    return response

def handle_userFlight():
    departure = request.form['departure']
    destination = request.form['destination']
    dateL = request.form['datelowerboundary']

    data = FlightModel.check_userflight(departure, destination, dateL.split("-")[0], dateL.split("-")[1],dateL.split("-")[2])
    email = request.cookies.get('email')
    response = make_response(render_template("userFlights.html", data=data))
    response.set_cookie('email', email)
    response.set_cookie("is_admin", "false")

    return response

