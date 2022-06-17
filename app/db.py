from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'yair'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
app.config['MYSQL_DATABASE_DB'] = 'chatapp'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)