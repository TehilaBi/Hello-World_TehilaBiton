from datetime import timedelta

from flask import Flask, redirect, url_for, render_template
from flask import request, session

app = Flask(__name__)
app.secret_key = '123'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


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
    loggedIn = ''
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
    if session['loggedIn'] == True:
        session.pop('username')
        session['loggedIn'] = False
    return redirect('/assignment9')


if __name__ == '__main__':
    app.run(debug=True)
