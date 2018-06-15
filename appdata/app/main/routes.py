from flask import render_template, flash, redirect, url_for, request, jsonify, current_app
from flask_login import current_user, login_required
from app.main import bp


@bp.route('/', methods=['GET', 'POST'])
def index():
  return redirect(url_for('auth.login'))

@bp.route('/main-page')
@login_required
def mainpage():
  return render_template('pages/index.pug', user=current_user)