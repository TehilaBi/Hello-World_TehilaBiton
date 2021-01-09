from datetime import timedelta

from flask import Flask, redirect, render_template, flash, blueprints, jsonify
from flask import request, session
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


@app.route('/')
def home():
    return render_template('Home page.html')


@app.route('/Projects')
def projects():
    return render_template('Projects Page.html')


@app.route('/Resume')
def resume():
    return render_template('Resume Page.html')


@app.route('/ContactMe')
def contact_me():
    return render_template('Contact Me Page.html')


@app.route('/ContactList')
def contact_list():
    return render_template('Contact List.html')


@app.route('/Hobbies')
def hobbies():
    nameMe = 'Tehila'
    return render_template('assignment8.html', name=nameMe,
                           hobbies=['Sport', 'Baking', 'travel'])


@app.route('/Tips for Bread')
def tips():
    nameMe = 'Tehila'
    return render_template('block.html', name=nameMe,
                           hobbies=['Sport', 'Baking', 'travel'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    loggedIn = False
    userEmail = ''
    search = False
    usersList = [{'name': 'Avi', 'Email': 'Avi@gmail.com'},
                 {'name': 'Gabi', 'Email': 'Gabi@gmail.com'}, {'name': 'Tehila', 'Email': 'Tehila@gmail.com'}]

    if request.method == 'GET':
        if 'name' in request.args:
            username = request.args['name']
            search = True
    if request.method == 'POST':
        username = request.form['username']
        session['loggedIn'] = True
        session['username'] = username
    return render_template('assignment9.html',
                           request_methods=request.method,
                           username=username, loggedIn=loggedIn, users=usersList, userEmail=userEmail, search=search)


@app.route('/Log_out')
def Log_out():
    if session['loggedIn']:
        session.pop('username')
        session['loggedIn'] = False
    return redirect('/assignment9')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                        passwd='root',
                                        database='webcvproject')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@app.route('/assignment11/users')
def users():
    if request.method == 'GET':
        query = "SELECT * FROM users"
        query_result = interact_db(query=query, query_type='fetch')
    return jsonify({'success': 'True', 'data': query_result})


@app.route('/assignment11/users/selected', defaults={'user_ID': 123})
@app.route('/assignment11/users/selected/<user_ID>')
def specificUser(user_ID):
    if request.method == 'GET':
        query = "SELECT * FROM users WHERE ID='%s'" % user_ID
        query_result = interact_db(query=query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({'success': 'False', 'data': []})
        else:
            return jsonify({'success': 'True', 'data': query_result[0]})


if __name__ == '__main__':
    app.run(debug=True)
