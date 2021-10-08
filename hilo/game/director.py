from game.dealer import dealer


class director:
    def __init__(self):
        # The class constructor
        # Define Game Start, and points
        self.game_on = True
        self.points = 300
        self.dealer = dealer()

    def game_start(self):
        while self.game_on:
            self.get_inputs()
            self.get_updates()
            self.do_outputs()

    def get_inputs(self):
        self.dealer.deal_cards()

    def get_updates(self):

        points = self.dealer.get_points()
        self.score += points

    def do_outputs(self):
        """
        Print out the current score.
        If they still have points to play then ask
        If they would like to continue playing.
        If they don't have points set game_on to False.
        """
        print(f"Your score is: {self.score}")

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
