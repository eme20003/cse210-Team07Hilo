from game.dealer import dealer
class director:
    
    def __init__(self):
        #The class constructor
        #Define Game Start, and points
        self.game_on = True
        self.points = 300
        self.dealer = dealer()

    def game_start(self):
        while self.game_on:
            self.get_inputs()
            self.get_updates()
            self.do_outputs()
    
    def get_inputs(self):
        pass
    #Heidi Wiseman

    def get_updates(self):
        
        points = self.dealer.get_points()
        self.score += points

    def do_outputs(self):
        pass
    #Ben Cornia

