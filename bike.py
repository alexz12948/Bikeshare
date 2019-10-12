'''
Definitions of a bike, which has an ID number, who the last user of the bike
was, when the bike was checked out (if it was taken out), and whether or not
it needs maintaince
'''

class Bike:
   
    '''Variables''' 
    ID = 0
    last_user = ""
    checkout_time = 0
    needs_maintenance = False
    
    '''Constructor'''
    def __init__(self, ID):
        self.ID = ID
        self.checkout_time = -1
        
    '''Updates the time that the bike was checked out'''
    def update_time(self, time):
        self.checkout_time = time

    '''sets a bike to be broken'''
    def broken(self):
        self.maintaince = True
