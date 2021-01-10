from flask import Blueprint, render_template
from flask import Flask, redirect,  flash
from flask import request, session
import mysql.connector


# about blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10',
                         template_folder='templates')


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


@assignment10.route('/assignment10', methods=['GET', 'POST'])
def ass10():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')

    if request.method == 'GET':
        if 'IdUserDelete' in request.args:
            IdUserDelete = request.args['IdUserDelete']
            query = "DELETE FROM users WHERE ID='%s';" % IdUserDelete
            interact_db(query, query_type='commit')

    if request.method == 'GET':
        if 'emailUserUpdate' in request.args:
            emailUserUpdate = request.args['emailUserUpdate']
            IdUserUpdate = request.args['IdUserUpdate']
            query = "UPDATE users SET Email = '%s' WHERE ID = '%s'" % (emailUserUpdate, IdUserUpdate)
            interact_db(query, query_type='commit')

    if request.method == 'POST':
        IdUser = request.form['IdUser']
        username = request.form['username']
        emailUser = request.form['emailUser']
        query = "INSERT INTO users(ID, NAME, Email) VALUES ('%s', '%s', '%s')" % (IdUser, username, emailUser)
        interact_db(query, query_type='commit')

    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)
