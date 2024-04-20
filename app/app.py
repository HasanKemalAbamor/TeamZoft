from flask import Flask, render_template
from Controller.RegistrationController import handle_registration

app = Flask(__name__,template_folder='templates')


@app.route('/register', methods=['GET'])
def show_register():
    return render_template('Registration.html')

@app.route('/register', methods=['POST'])
def post_register():
    return handle_registration()

@app.route('/login')
def login():
    return 'Login page not implemented yet.'

if __name__ == '__main__':
    app.run(debug=True)
