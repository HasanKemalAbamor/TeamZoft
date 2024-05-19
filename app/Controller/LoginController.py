from flask import request, session, redirect, url_for, flash, render_template, make_response
from Model.CheckUser import UserModel


def handle_login():
    email = request.form['email']
    password = request.form['password']
    if UserModel.check_user(email, password) == "ue":
        flash('User does not exist')
        return redirect(url_for('login'))
    elif UserModel.check_user(email, password) == "pw":
        flash('Password is wrong')
        return redirect(url_for('login'))
    else:
        emailChecked, is_admin = UserModel.check_user(email, password)
        if is_admin:
            return redirect(url_for('login'))
        else:
            response = make_response(render_template("logout.html", email=email))
            response.set_cookie('email', emailChecked)
            session['email'] = emailChecked
            return response

def handle_adminlogin():
    email = request.form['email']
    password = request.form['password']
    if UserModel.check_user(email, password) == "ue":
        flash('User does not exist')
        return redirect(url_for('login'))
    elif UserModel.check_user(email, password) == "pw":
        flash('Password is wrong')
        return redirect(url_for('login'))
    else:
        emailChecked, is_admin = UserModel.check_user(email, password)
        if is_admin:
            response = make_response(render_template("AdminPanel.html", email=email))
            response.set_cookie('email', emailChecked)
            response.set_cookie("is_admin", "true")
            session['email'] = emailChecked
            return response
        else:
            return redirect(url_for('adminlogin'))



def handle_logout():
    email = request.cookies.get('email')
    print(email + " : email")
    session.pop(email, None)
    return redirect("login")



