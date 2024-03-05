from flask import Blueprint, render_template, request, redirect, url_for, session

from exts import db
from models import User
from utils.pop_up import ShortInfo

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user is None or not user.get_pwd() == password:
            short_info = ShortInfo(info='Your username or password is incorrect, please try again!')
            return render_template('auth/login.html', short_info=short_info)
        
        session['uid'] = user.uid
        session['username'] = username
        
        return redirect(url_for('index.index'))


@bp.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        
        user = User.query.filter_by(username=username).first()
        if user is not None:
            short_info = ShortInfo('The username is already exist, please try another.')
            return render_template('auth/register.html', short_info=short_info)
        
        if not password == confirm:
            short_info = ShortInfo(info='Your password and confirmation do not match, please try again!')
            return render_template('auth/register.html', short_info=short_info)
        
        new_user = User(
            username=username,
            _User__password=password
        )
        db.session.add(new_user)
        db.session.commit()
        
        user = User.query.filter_by(username=username).first()
        
        return redirect(url_for('auth.login'))