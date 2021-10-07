from game.dealer import dealer
class director:
    
    def __init__(self):
        #The class constructor
        #Define Game Start, and points
        self.game_on = True
        self.points = 300
        self.dealer = dealer()



