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
        """
        Outputs the important game information for each round of play. In
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"\nYou rolled: {self.thrower.dice}")
        print(f"Your score is: {self.score}")
        if self.thrower.can_throw():
            choice = input("Roll again? [y/n] ")
            self.keep_playing = choice == "y"
        else:
            self.keep_playing = False
