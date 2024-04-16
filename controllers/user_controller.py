# controllers/user_controller.py
from flask import Blueprint, render_template, url_for, redirect, flash, session, request
from datetime import datetime
from models.User import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/Users')
def user():
    if 'loggedin' in session:
        data = User.get_all_users()
        render_args = {
                'data_user': data,
                'title': "Management User",
                'menu': 3,
            }      
        return render_template('admin/user/data_user.html', **render_args)
    flash('You are not logged in.', 'danger')
    return redirect(url_for('home'))

@user_bp.route('/Users/Insert', methods=['GET','POST'])
def insert_user():
    if request.method == 'POST' and 'loggedin' in session:
        name_user = request.form['name_user']
        phone_number = request.form['phone_number']
        username = request.form['username']
        position = request.form['position']
        password = request.form['password']
        password2 = request.form['pass_match']
        address = request.form['address']
        created_at = datetime.now()
        error = None

        # Validasi data
        if not name_user:
            error = 'name user is empty'
        if not username :
            error = 'username is empty'
        if  not phone_number :
            error = 'phone number is empty'
        if  not password and not password2 :
            error = 'Password is empty'
        if password != password2:
            error = 'Password not match'
        if position == 'not_select' :
            error = 'possition Not Select'
        if not address :
            error = 'address is empty'
        
        if error is not None :          
            flash(error, 'error')
            data = User.get_all_users()
            render_args = {
                'data_user': data,
                'title': "Management User",
                'menu': 3,
                'error': error,
                'name_user' : name_user,
                'username' : username,
                'phone_number' : phone_number,
                'position' : position,
                'password' : password,
                'address' : address
            }
            return render_template('admin/user/data_user.html', **render_args)
        else:
            User.add_user(name_user, username, phone_number, address, position, password, created_at)
            flash('Success! Data added', 'success')
            return redirect(url_for('user.user'))
    flash('You are not logged in.', 'danger')
    return redirect(url_for('home'))

# delete data
@user_bp.route('/User/Delete/<int:id>', methods=['GET'])
def delete_user(id):
    if 'loggedin' in session:
        User.delete_user(id)
        flash('Success! Data user deleted.','success')
        return redirect(url_for('user.user'))
    flash('You are not logged in.', 'danger')
    return redirect(url_for('home'))