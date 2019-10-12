'''
Sends information about bikes at the station to a server which will be displayed
on a website
'''

from bike import Bike
from flask import Flask, render_template, url_for, redirect, request
import flask_login
import json
import os

'''
create_list
Input: a bike
Output: a list of the bike's information
Does: creates a list and returns it
list[0] --> bike ID
list[1] --> last user
list[2] --> checkout_time
list[3] --> needs_maintenance
'''
def create_list(b):
    list = [b.ID, 
            b.last_user, 
            b.checkout_time, 
            b.needs_maintenance]

    return list

app = Flask(__name__)

test1 = Bike(1)
test2 = Bike(5)
test3 = Bike(9)

d = {1 : create_list(test1), 
     5 : create_list(test2), 
     9 : create_list(test3)}

print(json.dumps(d))

@app.route('/test_data')
def test_dat():
    return d

#--------------------------------------------------------#

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
           error = "INVALID CREDENTIALS"
        else:
            return redirect(url_for('print'))

    return render_template('login.html', error=error)

@app.route('/test')
def print():
    return "Was able to successfully login"

if __name__ == '__main__':
    app.run()