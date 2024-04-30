
from flask import request, redirect, url_for, flash, render_template
from Model.AddUser import UserModel


def handle_registration():
    """Process the submitted registration form data on POST request."""
    # Process the submitted form data
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    phone = request.form['PhoneNumber']
    password = request.form['password']  # Remember to hash this password in production

    # Use the UserModel class to add a new user to the database
    UserModel.add_user(name, surname, email, phone, password)

    # Redirect to a different page, e.g., a login page, or back to home
    flash('Registration successful. Please log in.', 'success')
    return redirect(url_for('login'))

# Other controller functions can be added here as well
