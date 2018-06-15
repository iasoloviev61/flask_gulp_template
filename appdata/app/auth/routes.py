from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from app.models import User
from app.auth.email import send_password_reset_email

@bp.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.mainpage'))
  form = LoginForm()
  if form.validate_on_submit():
    email = User.query.filter_by(email=form.email.data).first()
    if email is None or not email.check_password(form.password.data):
      flash('invalid username or password')
      return redirect(url_for('auth.login'))
    # return redirect(url_for('mainpage'))
    login_user(email)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('main.mainpage')
    print(next_page)
    return redirect(next_page)
  return render_template('pages/auth/login.pug', myform=form)

@bp.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('auth.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.mainpage'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash("you are now register")
    return redirect(url_for('auth.login'))
  return render_template('pages/auth/register.pug', myform=form)

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
  if current_user.is_authenticated:
    return redirect(url_for('main.mainpage'))
  form = ResetPasswordRequestForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user:
      send_password_reset_email(user)
    flash('Check your email for the instructions to reset your password')
    return redirect(url_for('auth.login'))
  return render_template('pages/auth/reset_password_request.pug',
                         title='Reset Password', myform=form)

@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
  if current_user.is_authenticated:
    return redirect(url_for('main.mainpage'))
  user = User.verify_reset_password_token(token)
  if not user:
    return redirect(url_for('auth.login'))
  form = ResetPasswordForm()
  if form.validate_on_submit():
    user.set_password(form.password.data)
    db.session.commit()
    flash('Your password has been reset.')
    return redirect(url_for('auth.login'))
  return render_template('pages/auth/resetpassword.jade', myform=form)
