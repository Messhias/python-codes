from random import randint

class Die():
    ''' A CLASS WICH REPRESENTES ONE DICE '''

    def __init__(self,num_slides=6):
        self.num_slides=num_slides

    def roll(self):
        return randint(1,self.num_slides)
