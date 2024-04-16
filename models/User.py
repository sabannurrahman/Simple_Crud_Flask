# models/user.py
from database import mysql
from werkzeug.security import check_password_hash, generate_password_hash
class User:
    @staticmethod
    def get_all_users():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tb_user ORDER BY id DESC")
        data = cur.fetchall()
        cur.close()
        return data
    
    def add_user(name_user, username, phone_number, address, position, password, created_at):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tb_user (name_user, username, phone_number, address, isAdmin, password, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name_user, username, phone_number, address, position, generate_password_hash(password), created_at))
        mysql.connection.commit()
        cur.close()
    
    def delete_user(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tb_user WHERE id=%s", (id,))
        mysql.connection.commit()

    def count_user():
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM tb_user") 
        total_count = cur.fetchone()[0]
        cur.close()
        return total_count