# controllers/user_controller.py
from flask import Blueprint, render_template, url_for, redirect, flash, session, request
from datetime import datetime
from models.Item import Item
import os

item_bp = Blueprint('item', __name__)

@item_bp.route('/Items')
def AllItem():
    if 'loggedin' in session:
        data = Item.get_all_items()
        render_args = {
                'data_item': data,
                'title': "Management Ites",
                'menu': 2,
            }      
        return render_template('admin/item/data_item.html', **render_args)
    flash('You are not logged in.', 'error')
    return redirect(url_for('home'))


# insert data
@item_bp.route('/Items/Insert', methods=['GET','POST'])
def insert_item():
    if request.method == 'POST' and 'loggedin' in session:
        name_item = request.form['name_item']
        price = request.form['price']
        stok = request.form['stok2']
        unit = request.form['unit']
        gambar = request.files['gambar']
        description = request.form['descrip']
        created_at = datetime.now()
        error = None
        # Validasi data
        if not name_item:
            error = 'name item is empty'
        if not price :
            error = 'price is empty'
        if not stok :
            error = 'stok is empty'
        if unit == 'notSelect' :
            error = 'Unit Not Select'
        if not description :
            error = 'description is empty'

        if error is not None :          
            flash(error, 'error')
            data = Item.get_all_items()
            render_args = {
                'data_item': data,
                'title': "Management Items",
                'menu': 2,
                'error': error,
                'name_item' : name_item,
                'stok' : stok,
                'unit' : unit,
                'price' : price,
                'unit' : unit,
                'description' : description
            }
            return render_template('admin/item/data_item.html', **render_args)
        else:
            file_path = os.path.join( 'static', 'uploads', gambar.filename)
            gambar.save(file_path)
            image = gambar.filename
            Item.add_item(name_item, price, stok, unit, image, created_at, description)
            flash('Success! Data added', 'success')
            return redirect(url_for('item.AllItem'))
    flash('You are not logged in.', 'error')
    return redirect(url_for('home'))


# Update data
@item_bp.route('/Items/Update', methods=['POST'])
def update_item():
    if request.method == 'POST' and 'loggedin' in session:
        id = request.form['id']
        name_item = request.form['name_item3']
        price = request.form['price3']
        unit = request.form['unit3']
        stok = request.form['stok3']
        description = request.form['descript4']   
        Item.edit_item(name_item, price,stok, unit, description, id)
        flash('Success! Data updated.', 'success')
        return redirect(url_for('item.AllItem'))
    flash('You are not logged in.', 'error')
    return redirect(url_for('home'))

# delete data
@item_bp.route('/Items/Delete/<int:id>', methods=['GET'])
def delete_item(id):
    if 'loggedin' in session:
        Item.delete_item(id)
        flash('Success! Data deleted.', 'success')
        return redirect(url_for('item.AllItem'))
    flash('You are not logged in.', 'error')
    return redirect(url_for('home'))
