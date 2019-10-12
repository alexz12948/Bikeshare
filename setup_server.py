'''
Sends information about bikes at the station to a server which will be displayed
on a website
'''

NUM_BIKES = 30

from bike import Bike
from flask import Flask, render_template, url_for, redirect, request
from configparser import ConfigParser
import json
from random import randint

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

'''
random_bike_data
Input: N/A
Output: a dictionary of bikes
Does: creates a dictionary of random bike data
'''
def random_bike_data():
    list = [0] * NUM_BIKES
    for i in range(NUM_BIKES):
        list[i] = randint(1, 101)

    bikes = {}
    for i in range(NUM_BIKES):
        bikes[list[i]] = create_list(Bike(list[i]))

    return bikes

'''
check_user
Inputs: the config file and a name/password in the form of a string
Output: a boolean
Does: determines whether or not the name and password exist and 
      are linked together
'''
def check_user(cfg, name, password):
    if name in cfg['admins']:
        if cfg['admins'][name] == password:
            return True

    if name in cfg['users']:
        if cfg['users'][name] == password:
            return True

    return False


app = Flask(__name__)
cfg = ConfigParser()

cfg.read('users.cfg')

d = random_bike_data()

#--------------------------------------------------------#

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    error = None

    if request.method == 'POST':
        if not check_user(cfg, request.form['username'], request.form['password']):
           error = "INVALID CREDENTIALS"
        elif request.form['username'] in cfg['admins']:
            return redirect(url_for('admins'))
        else:
            return redirect(url_for('client'))

    return render_template('login.html', error=error)

@app.route('/admins')
def admins():
    return "You are an admin"

@app.route('/useable_bikes')
def client():
    return "Bikes!"

@app.route('/test_data')
def test_data():
    return json.dumps(d)

if __name__ == '__main__':
    app.run()