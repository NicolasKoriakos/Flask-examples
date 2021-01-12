from re import M
from flask import Flask, render_template
from flask.globals import request
from flask_mysql_connector import MySQL
from mysql.connector import cursor

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DATABASE'] = 'users'

# app.config['MYSQL_PASSWORD'] = 'contra1234'
# app.config['MYSQL_PORT'] = 2020
# app.config['MYSQL_HOST'] = '172.16.0.3'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO user_data (name,mail) values (%s, %s)', (username, email))
        mysql.connection.commit()
        cursor.close()

        return 'Datos cargados!'

    return render_template('index.html')


if __name__ == '__main__':

    app.run(debug=True)