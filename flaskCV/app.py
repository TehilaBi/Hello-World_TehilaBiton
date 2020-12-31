from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


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


@app.route('/Block')
def block():
    nameMe = 'Tehila'
    return render_template('block.html', name=nameMe,
                           hobbies=['Sport', 'Baking', 'travel'])


if __name__ == '__main__':
    app.run(debug=True)
