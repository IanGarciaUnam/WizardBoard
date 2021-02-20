from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Session
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup.html')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'
@auth.route('/signup', methods=['POST'])
def sign_post():
	return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['POST'])
def signup_post():
	"""
	Problema , código no registrado o leído
	"""
	username=request.form.get('username')
	#name=request.form.get('name')
	password=request.form.get('password')

	course= Session.query.filter_by(password=generate_password_hash(password, method='sha256'))

	if course:
		flash("Code to join to your session already exists")
		return redirect(url_for('auth.signup'))
	#Create a new session
	new_course = Session(username=username, password=generate_password_hash(password, method='sha256'))
	# add the new user to the database
	db.session.add(new_course)
	db.session.commit()
	return redirect(url_for('auth.login'))
