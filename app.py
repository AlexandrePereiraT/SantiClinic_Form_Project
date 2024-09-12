import sqlite3
import smtplib
from flask import Flask, render_template, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config['DEBUG'] = True


def get_db_conn():
    conn = sqlite3.connect('Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def render_form():
    return render_template('form.html')


@app.route('/complete', methods=['GET'])
def write_db():
    f_name = request.args.get('fname')
    l_name = request.args.get('lname')
    email = request.args.get('email')
    satisfaction = request.args.get('satisfaction')
    needs = request.args.get('needs')
    quality = request.args.get('quality')
    recommend = request.args.get('recommend')
    name = f_name + ' ' + l_name

    print(f'''
    First name: {f_name};
    Last name: {l_name};
    Full name: {name};
    E-mail: {email};
    Satisfaction: {satisfaction};
    Needs: {needs};
    Quality: {quality};
    Recommend: {recommend};''')

    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Information ("name", "e-mail", "satisfaction", "needs", "quality", "recommend") VALUES (?, ?, ?, ?, ?, ?)',
        (name, email, satisfaction, needs, quality, recommend))
    conn.commit()
    conn.close()

    return render_template('complete.html')


if __name__ == '__main__':
    app.run(debug=True)