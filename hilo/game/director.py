from game import dealer


class Director:
    def __init__(self):
        # The class constructor
        # Define Game Start, and points
        self.game_on = True
        self.points = 300
        self.dealer = dealer.Dealer()

    def game_start(self):
        while self.game_on:
            self.get_inputs()
            self.get_updates()
            self.do_outputs()

    def get_inputs(self):
        #Gets the inputs at the beginning of each round of play. In this case,
        #that means dealing the cards.

        #Args:
            #self (Dealer): An instance of Dealer.
            
        self.dealer.deal_cards()

    def get_updates(self):
        # Author: Daniel Emerson
        # Calling the get_points method from the dealer class
        # From the returned value this saves the points and adds any future points that may occur
        # to have a grand total score
        points = self.dealer.get_points()
        self.points += points

    def do_outputs(self):
        """
        Print out the current score.
        If they still have points to play then ask
        If they would like to continue playing.
        If they don't have points set game_on to False.
        """
        print(f"Your score is: {self.points}")

        # Return value of can_deal method.
        deal = self.dealer.can_deal()

        # Check if deal is True or False.
        if deal == True:
            choice = input("Keep playing [y/n] ")
            if choice == "y":
                self.game_on = True
            else:
                self.game_on = False
        else:
            self.game_on = False
