from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return"<P>LOGININ</P>"
@auth.route('/logout')
def logout():
    return"<p>LogOut</p>"
@auth.route('/sign-up')
def sign_up():
    return"<p>sign-up</p>"
