import os, random, uuid, string
from functools import wraps
import requests
from uuid import uuid4
from datetime import datetime
from functools import wraps
from flask_wtf.csrf import CSRFProtect
from flask import render_template,request,redirect,flash,url_for,make_response,session,flash,jsonify,request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import  Message
from pkg import app, mail
from pkg.models import db,State,Category,PropertyType,Lga,Property,Orders,Image,Admin,NewsletterSubscriber,ContactUs,User
from pkg.adminlogin_forms import AdminloginForm
from pkg.searchuser_forms import SearchuserForm
from pkg.userdetails_forms import UserdetailsForm


def login_required(f):
    @wraps(f) 
    def check_login(*args, **kwargs):
        if session.get('useronline') != None:
            return f(*args, **kwargs)
        else:
            flash('You must be logged in to access this page',category='error')
            return redirect(url_for('login'))
    return check_login



@app.route('/users/profile/')
def users_profile():
    users = User.query.all()  
    return render_template('admin/user_profile.html', users=users)



            

@app.route('/admin/dashboard/')
def admin_dashboard():
    admin_id = session.get('useronline')
    admin = Admin.query.get(admin_id)
    return render_template('admin/admin_dashboard.html', admin=admin)




NIN_VALIDATION_API_URL = "https://api.example.com/nin/validation"


@app.route("/validate/user/nin", methods=["POST"])
def validate_user_nin():
    # Get user data from the registration form
    nin = request.form.get("NIN")
    fname = request.form.get("First Name")
    lname = request.form.get("Last Name")
    dob = request.form.get("Date of Birth")

    # Make a request to the NIN validation API
    payload = {
        "id": nin,
        "isSubjectConsent": True,
        "validations": {
            "data": {
                "lastName": lname,
                "firstName": fname,
                "dateOfBirth": dob
            }
        }
    }
    response = requests.post(NIN_VALIDATION_API_URL, json=payload)

    # Handle the API response
    if response.status_code == 200:
        validation_result = response.json()
        if validation_result["success"]:
            # Validation successful, update your database or take other actions
            # For example:
            # user.update(validation_status=True)
            return jsonify({"message": "NIN validation successful"})
        else:
            # Validation failed, handle accordingly
            return jsonify({"error": "NIN validation failed"})
    else:
        # Handle API error
        return jsonify({"error": "Failed to validate NIN"})




@app.route('/admin/index/')
def admin_home():
    return render_template("admin/admin_index.html")


@app.route('/admin/login/', methods = ['POST','GET'])
def admin_login():
    form = AdminloginForm()
    if request.method=='POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            data = db.session.query(Admin).filter(Admin.admin_username==username).first()
            if data:
                password= data.admin_password
                rsp = password
                if rsp:
                    id = data.admin_id
                    session['useronline'] = id
                    session['name'] = data.admin_username
                    return redirect('/admin/dashboard/')
                else:
                    flash('Invalid Login Credentials', 'error')
                    return render_template('admin/admin_login.html',form=form)
            else:
                flash('Please enter valid credentials', 'error')
                return redirect('/adminlogin/')
        else:
            return redirect('/adminlogin/')   
    else:
        return render_template('admin/admin_login.html', form=form)




@app.route('/admin/logout/')
def admin_logout():
    return render_template("admin/admin_index.html")
 
@app.route("/exit/")
def exit():
    session.pop("useronline",None)
    return redirect("/admin/dashboard/")

@app.route('/user/dashboard/')
def user_dashboard():
    user_id = session.get('useronline')
    user = User.query.get(user_id)
    return render_template('admin/user_details.html', user=user)


@app.route('/display/user/profile/', methods=['POST', 'GET'])
def get_user_details():
    form = UserdetailsForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            ref = form.ref.data
            user = db.session.query(User).filter(User.user_email == email, User.user_ref == ref).first()
            if user:
                id = user.user_id
                session['useronline'] = id
                session['name'] = user.user_fname
                return redirect('/user/dashboard/')
            else:
                flash('Invalid user credentials', 'error')
                return render_template('admin/search_user.html', form=form)
        else:
            flash('Invalid form submission', 'error') 
            return render_template('admin/admin_dashboard.html', form=form) 
    else:
        return render_template('admin/search_user.html', form=form)


