from datetime import datetime
from sqlalchemy import Index, ForeignKeyConstraint
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()




class State(db.Model):
    state_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    state_name = db.Column(db.String(120),index=True, nullable=False)
    lga_id = db.relationship('Lga', backref='state', lazy=True)
    

    

class Lga(db.Model):
    lga_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    lga_name = db.Column(db.String(120),index=True, nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('state.state_id'), nullable=False)
    properties = db.relationship('Property', backref='lga', lazy=True)


class Property(db.Model):
    property_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    property_name = db.Column(db.String(100), index=True, nullable=False)
    property_description = db.Column(db.Text, index=True, nullable=False)
    property_status = db.Column(db.Enum('available', 'not available'), nullable=True)
    property_added_on = db.Column(db.DateTime(), default=datetime.utcnow)
    property_price = db.Column(db.String(120))
    property_address = db.Column(db.Text)
    property_ref = db.Column(db.String(36),nullable=False, unique=True)
    property_category = db.Column(db.Integer(), db.ForeignKey('category.cat_id'))
    property_state = db.Column(db.Integer(), db.ForeignKey('state.state_id'))
    property_lga = db.Column(db.Integer, db.ForeignKey('lga.lga_id'))
    property_user_id = db.Column(db.Integer(), db.ForeignKey('user.user_id'))    
    images = db.relationship('Image', backref='property')
    property_type = db.Column(db.Integer, db.ForeignKey('property_type.type_id'))
    



class PropertyType(db.Model):
    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), nullable=False, unique=True)
    properties = db.relationship('Property', backref='property_types', lazy=True)
    

class User(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_fname = db.Column(db.String(200), nullable=False)
    user_lname = db.Column(db.String(200), nullable=False)
    user_othername = db.Column(db.String(200), nullable=True)
    user_dob = db.Column(db.Date)
    user_address = db.Column(db.Text, nullable=False)
    user_phone = db.Column(db.String(20), nullable=False, unique=True)
    user_nin = db.Column(db.String(20), nullable=False, unique=True)
    user_pics = db.Column(db.String(120),nullable=True)
    user_email = db.Column(db.String(120), nullable=False, unique=True)
    user_password = db.Column(db.String(200), nullable=False)
    user_datereg = db.Column(db.DateTime(), default=datetime.utcnow)
    user_state = db.Column(db.Integer(), db.ForeignKey('state.state_id'))
    user_lga = db.Column(db.Integer, db.ForeignKey('lga.lga_id'))
    properties = db.relationship('Property', backref='user', lazy=True)
    images = db.relationship('Image', backref='user_relation', lazy=True)
    userstate = db.relationship('State',backref='user', lazy=True)
    userlga = db.relationship('Lga', backref='user',lazy=True)
    user_ref = db.Column(db.String(10),nullable=False, unique=True)

    


class Category(db.Model):
    cat_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    cat_name = db.Column(db.String(50), nullable=False)
    property = db.relationship('Property', backref='categories')


class Orders(db.Model):
    orders_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    orders_amount = db.Column(db.String(120))
    orders_date = db.Column(db.DateTime(), default=datetime.utcnow)
    orders_statue = db.Column(db.Enum('1', '0'), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.user_id'))  
    user = db.relationship('User', backref=db.backref('orders', lazy=True))



class Image(db.Model):
    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    image_name = db.Column(db.String(100), nullable=False)
    property_id = db.Column(db.Integer(), db.ForeignKey('property.property_id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.user_id'))  
    user = db.relationship('User', backref='users', lazy=True)


class Admin(db.Model):
    admin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    admin_name = db.Column(db.String(100), nullable=False)
    admin_username = db.Column(db.String(100), nullable=False)
    admin_password = db.Column(db.String(100), nullable=False)
    admin_lastlogin = db.Column(db.DateTime(), default=datetime.utcnow)


class NewsletterSubscriber(db.Model):
    subscriber_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_subscribed = db.Column(db.DateTime(), default=datetime.utcnow)

class ContactUs(db.Model):
    contact_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    contact_fname = db.Column(db.String(100), nullable=False)
    contact_lname =db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(120), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)
    contact_message = db.Column(db.Text, nullable=False)
    contact_date = db.Column(db.DateTime(), default=datetime.utcnow)


    
    

    






