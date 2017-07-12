from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True



def empty_field(fields):
    if len(fields)>0:
        return True
    else:
        return False

def validate_field(fields):
    if " " not in fields:
        if len(fields) >3 and len(fields)<20:
            return True
    else:
        return False

def match(p_one, p_two):
    if p_one == p_two:
        return True
    else:
        return False

def vmail(mail_field):
    if "@" and "." not in mail_field:
        return False
    elif " " in mail_field:
        return False
    elif len(mail_field)<3 or len(mail_field)>20:
        return False
    else:
        return True



@app.route("/")
def index():
    return render_template('User_Signup.html')


@app.route("/signup", methods = ['POST'])
def signup():
    usrname=request.form['usrname']
    passwrd=request.form['passwrd']
    vpasswrd=request.form['vpasswrd']
    email=request.form['email']
    usrname_error=''
    passwrd_error=''
    vpasswrd_error=''
    error_count = 0

    if not empty_field(usrname):
        usrname_error="Enter a valid username."
        error_count=error_count+1

    if not empty_field(passwrd):
        passwrd_error="Enter a valid password."
        error_count=error_count+1

    if not empty_field(vpasswrd):
        vpasswrd_error="Password must be verified."
        error_count=error_count+1

    if not validate_field(usrname):
        usrname_error="Enter a valid username."
        error_count=error_count+1

    if not validate_field(passwrd):
        passwrd_error="Enter a valid password"
        error_count=error_count+1

    if not match(passwrd, vpasswrd):
        vpasswrd_error="Passwords must match!"
        error_count=error_count+1

    if not vmail(email):
        email_error="Please enter a valid email."
        error_count=error_count+1

    if error_count > 0: 
        return render_template('User_Signup.html', usrname=usrname, passwrd='', vpasswrd='', email=email,
                                usrname_error=usrname_error, passwrd_error=passwrd_error, vpasswrd_error=vpasswrd_error,
                                email_error=email_error)

    else:
        return render_template('welcome.html', usrname=usrname)



app.run()
