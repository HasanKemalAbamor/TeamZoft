from flask import Flask, render_template, request, redirect, url_for, session
from Controller.RegistrationController import handle_registration
from Controller.LoginController import handle_login, handle_logout
from flask_login import LoginManager, login_required

app = Flask(__name__, template_folder='templates')
app.secret_key = "d6g8"



@app.route('/register', methods=['GET'])
def show_register():
    return render_template('Registration.html')


@app.route('/register', methods=['POST'])
def post_register():
    return handle_registration()


@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def post_login():
    return handle_login()


@app.route('/logout', methods=['GET'])
def logout():
    return render_template("logout.html")


@app.route('/logout', methods=['POST'])
def logout_user():
    return handle_logout()


@app.before_request
def check_logged_in():
    if request.endpoint != 'login' and 'logged_in' not in session:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
