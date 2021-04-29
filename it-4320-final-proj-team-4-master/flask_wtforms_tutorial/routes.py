from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *

    
#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    
    form = AdminLoginForm()
    if request.method == 'POST':
        #Get the form data
        username = request.form['username']
        password = request.form['password']
        #Match the user infomation format in txt file 
        userinfo = username + ", "+ password +"\n"
        chart = None
        try:
            file = open('passcodes.txt','r')
        except FileNotFoundError:
            err = "ERROR: Can't find file."
        else:
            contents = file.readlines()
            
        for content in contents:
            if (content == userinfo):
                err =None
                chart = seatchart()
                break
            err = "Bad username/password combination. Try again"

        return render_template("admin.html", form=form, template="form-template",err = err, chart = chart)   

    return render_template("admin.html", form=form, template="form-template" )

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")

def seatchart():
    chart = [['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O']]
             
    try:
        file = open('reservations.txt','r')
    except FileNotFoundError:
        err = "ERROR: Can't find file."
    else:
        reservations = file.readlines()
    for  reservation in reservations:
        row = int(reservation.split(', ')[1])
        seat = int(reservation.split(', ')[2])
        chart[row][seat] = 'X'
    return chart