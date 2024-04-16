# controllers/user_controller.py
from database import mysql
from flask import Blueprint, render_template, url_for, redirect, flash, session, request
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM tb_user WHERE username=%s', (username,))
        akun = cur.fetchone() 
        if akun is None:
            flash('Check Usename and Password', 'error')
            return redirect(url_for('home'))
        elif not check_password_hash(akun[6], password) :
            flash('Check Your Password', 'error')
            return redirect(url_for('home'))
        else:
            if akun[5] == 'Admin':
                session['loggedin'] = True
                session['id_user'] = akun[0]
                session['isAdmin'] = akun[5]
                session['name_user'] = akun[1]
                return redirect(url_for('dashboard.admin'))
            elif akun[5] == 'Pegawai':
                session['loggedin'] = True
                session['id_user'] = akun[0]
                session['isAdmin'] = akun[5]
                session['name_user'] = akun[1]
                return redirect(url_for('dashboard.pegawai'))
            else:
                return redirect(url_for('home'))
   
    return render_template('login.html')

@login_bp.route('/Logout')
def Logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('isAdmin', None)
    session.pop('name_user', None)
    return redirect(url_for('home'))