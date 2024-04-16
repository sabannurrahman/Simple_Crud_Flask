from flask import Blueprint, render_template, url_for, redirect, flash, session, request
from models.Item import Item
from models.User import User


dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/Admin_Dashboard')
def admin():
    if 'loggedin' in session:
        title = "Dashboard Admin"
        total_item = Item.count_item()
        total_user = User.count_user()
        return render_template('admin/dashboard/dashboard.html', menu=1, total_item=total_item, total_user=total_user)
    flash('You are not logged in.', 'error')
    return redirect(url_for('home'))

@dashboard_bp.route('/Pegawai_Dashboard')
def pegawai():
    if 'loggedin' in session:
        title = "Dashboard Pegawai"
        return render_template('pegawai/dashboard/dashboard.html', menu=1)
    flash('You are not logged in.', 'error')
    return redirect(url_for('home'))