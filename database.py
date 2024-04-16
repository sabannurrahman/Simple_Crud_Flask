from flask import Flask
from flask_mysqldb import MySQL

# Database Configuration
app = Flask(__name__)
app.secret_key = 'tokosaban'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_toko'

mysql= MySQL(app)