from flask import Flask, render_template, request, redirect, url_for, session, make_response

from Controller.FlightsController import handle_addFlight, handle_searchFlight, handle_sortFlight, handle_editFlight, \
    handle_deleteFlight
from Controller.LoginController import handle_logout, handle_login, handle_adminlogin
from Controller.RegistrationController import handle_registration
from Model.CheckLogout import CheckUserModel

app = Flask(__name__, template_folder='templates')
app.secret_key = "d6g8"


@app.route('/register', methods=['GET'])
def show_register():
    response = make_response(render_template('Registration.html'))
    response.set_cookie('email', '', expires=0)
    return response


@app.route('/register', methods=['POST'])
def post_register():
    return handle_registration()


@app.route('/login', methods=['GET'])
def login():
    response = make_response(render_template("login.html"))
    response.set_cookie('email', '', expires=0)
    return response


@app.route('/login', methods=['POST'])
def post_login():
    return handle_login()


@app.route('/logout', methods=['GET'])
def logout():
    return render_template("logout.html")


@app.route('/logout', methods=['POST'])
def logout_user():
    return handle_logout()


@app.route('/adminlogin', methods=['GET'])
def adminlogin():
    response = make_response(render_template("AdminLogin.html"))
    response.set_cookie('email', '', expires=0)
    return response


@app.route('/adminlogin', methods=['POST'])
def post_adminlogin():
    return handle_adminlogin()


@app.route('/adminpanel', methods=['GET'])
def adminPanel():
    return render_template("adminpanel.html")


@app.route('/addflight', methods=['GET'])
def addflight():
    email = request.cookies.get("email")
    if CheckUserModel.check_admin(email):
        return render_template("addFlight.html")
    else:
        return redirect("adminlogin")


@app.route('/addflight', methods=['POST'])
def post_addflight():
    email = request.cookies.get("email")
    if CheckUserModel.check_admin(email):
        return handle_addFlight()
    else:
        return redirect("adminlogin")


@app.route('/viewflights', methods=['GET'])
def viewflights():
    email = request.cookies.get("email")
    if CheckUserModel.check_admin(email):
        return handle_searchFlight()
    else:
        return redirect("adminlogin")


@app.route('/flight_details/<string:flight_id>', methods=['GET', 'POST'])
def flight_details(flight_id):
    email = request.cookies.get("email")
    if CheckUserModel.check_admin(email):
        if request.method == 'GET':
            return render_template("EditFlight.html", flight_id=flight_id)
        elif request.method == 'POST':
            return handle_editFlight(flight_id)
    else:
        return redirect("adminlogin")


@app.route('/flight_details/<string:flight_id>/delete', methods=['POST'])
def delete_flights(flight_id):
    email = request.cookies.get("email")
    print("sdadsads")
    if CheckUserModel.check_admin(email):
        return handle_deleteFlight(flight_id)
    else:
        return redirect("adminlogin")


@app.route('/userpanel', methods=['GET'])
def userpanel():
    email = request.cookies.get("email")
    if CheckUserModel.check_user(email):
        return render_template("Logout.html", data="")
    else:
        return redirect("login")


@app.route('/userFlights', methods=['GET'])
def userFlights():
    email = request.cookies.get("email")
    if CheckUserModel.check_user(email):
        return render_template("userFlights.html", data="")
    else:
        return redirect("login")


@app.route('/userFlights', methods=['POST'])
def post_userFlights():
    email = request.cookies.get("email")
    if CheckUserModel.check_user(email):
        return handle_sortFlight()
    else:
        return redirect("login")

@app.route('/select_seat', methods=['GET'])
def selectseat():
    email = request.cookies.get("email")
    if CheckUserModel.check_user(email):
        return render_template("seatSelection.html")
    else:
        return redirect("adminlogin")

@app.route('/payment', methods=['GET'])
def payment():
    email = request.cookies.get("email")
    if CheckUserModel.check_user(email):
        print("dsadsasda")
        return render_template("payment.html")
    else:
        return redirect("adminlogin")


if __name__ == '__main__':
    app.run(debug=True)
