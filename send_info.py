'''

'''

from bike import Bike
import json

def create_list(b):
    list = [b.ID, 
            b.last_user, 
            b.checkout_time, 
            b.needs_maintenance]

    return list

test1 = Bike(1)
test2 = Bike(5)
test3 = Bike(9)

d = {1 : test1, 
     5 : test2, 
     9 : test3}

