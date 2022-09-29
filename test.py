from flask import Flask, render_template, request, redirect, app

import pymysql

test = Flask(__name__)

conn = pymysql.connect(host='localhost', user='root', password='Akhil@123', db='flaskapp')


@test.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        city = userDetails['city']
        cur = conn.cursor()
        sql = '''insert into `users` (name, email, city)
                 values (%s, %s, %s) 
              '''
        cur.execute(sql, (name, email, city))
        conn.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')


@test.route('/users')
def users():
    cur = conn.cursor()
    resultValue = cur.execute("SELECT * FROM USERS")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)


if __name__ == '__main__':
    test.run(port=8000)
