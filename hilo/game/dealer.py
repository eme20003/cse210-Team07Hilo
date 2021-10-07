from game.director import director
import random

#The class constructor
        #Define deal cards, get points, can deal, init 

class dealer:

    def __init__(self):
        self.current_card = 0
        self.next_card = 0
    
    def deal_cards(self):
        self.current_card = random.randint(1,13)
        self.next_card = random.randint(1,13)

    def get_points(self):
        pass
    #Mitchel Ball
    
    def can_deal(self):
        pass
    #Morgan Allen