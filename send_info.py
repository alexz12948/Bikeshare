'''
Sends information about bikes at the station to a server which will be displayed
on a website
'''

from bike import Bike
from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from login import LoginForm
import json
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'bikeshare'

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

test1 = Bike(1)
test2 = Bike(5)
test3 = Bike(9)

d = {1 : create_list(test1), 
     5 : create_list(test2), 
     9 : create_list(test3)}

@app.route('/')
def print_dictionary():
    return d

if __name__ == '__main__':
    app.run()