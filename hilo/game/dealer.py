import random

# The class constructor
# Define deal cards, get points, can deal, init


class dealer:
    pass

    def __init__(self):
        self.current_cards = []
        self.score = 0

    def deal_cards(self):
        card1 = random.randint(1, 13)
        card2 = random.randint(1, 13)
        self.current_cards = [card1, card2]

    def get_points(self):
        """Calulate the points earned for an individual guess.
        Correct = +100
        Incorrect = -100
        Author: Mitchell Ball
        """
        if self.current_cards[0] > self.current_cards[1]:
            self.score = self.score - 75

        elif self.current_cards[0] < self.current_cards[1]:
            self.score = self.score + 100

        return self.score

    def can_deal(self):
        # Checks to see if the player has lost the game
        # and if they whish to continue
        # Is to be used in an IF statement
        # return (self.director.points != 0 )
        # Morgan Allen

        pass
