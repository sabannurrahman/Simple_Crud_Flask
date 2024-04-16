# models/user.py
from database import mysql

class Item:
    @staticmethod
    def get_all_items():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tb_item ORDER BY id DESC")
        data = cur.fetchall()
        cur.close()
        return data
    
    def add_item(name_item, price, stok, unit, image, created_at, description):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tb_item (name_item, price, stok, unit, image, created_at, description) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name_item, price, stok, unit, image, created_at, description))
        mysql.connection.commit()
        cur.close()

    def edit_item(name_item, price, stok, unit, description, id):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tb_item SET name_item=%s, price=%s, stok=%s, unit=%s, description=%s WHERE id=%s", (name_item, price,stok, unit, description, id))
        mysql.connection.commit()
        cur.close()
    
    def delete_item(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tb_item WHERE id=%s", (id,))
        mysql.connection.commit()
        cur.close()
    
    def count_item():
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM tb_item") 
        total_count = cur.fetchone()[0]
        cur.close()
        return total_count
